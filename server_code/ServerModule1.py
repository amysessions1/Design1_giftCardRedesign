import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from random import randrange

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.


@anvil.server.callable
def add_business(business_info):
  #business_info should be a list of info in the form [{business name}, {business_username}, {business_password}] all as strings
  #generate business_id
  add_data={}
  business_id = randrange(1000000000000000,9999999999999999)
  #check if business_id is already assigned to another business
  while app_tables.business_data.get(businessID=business_id) is not None:
    business_id = randrange(1000000000000000,9999999999999999)
  add_data["businessID"] = business_id
  #check for unique username
  if app_tables.business_data.get(username=business_info[1]) is not None:
    return -1
  add_data["Name"] = business_info[0]
  add_data["username"] = business_info[1]
  add_data["password"] = business_info[2]
  #add business to business_data
  app_tables.business_data.add_row(**add_data)
  #add business to balances table
  app_tables.balances.add_row(business=business_id, user_data={}, unlinked={})
  # balances.append([])
  # #add business to unlinked_balances
  # unlinked_balances.append([])
  print(f"new business {business_info[1]} added")
  return 0



@anvil.server.callable
def add_user(user_info):
  #user_info should be a list of info in the form [{user name}, {user_username}, {user_password}, {phone number}] all as strings
  #generate user_id
  add_data={}
  user_id = randrange(1000000000000000,9999999999999999)
  #check if user_id is already assigned to another user
  while app_tables.user_data.get(userID=user_id) is not None:
    user_id = randrange(1000000000000000,9999999999999999)
  add_data["userID"] = user_id
  #check for unique username
  if app_tables.user_data.get(username=user_info[1]) is not None:
    return -1
  add_data["Name"] = user_info[0]
  add_data["username"] = user_info[1]
  add_data["password"] = user_info[2]
  add_data["phone"] = user_info[3]
  #add user to user_data
  app_tables.user_data.add_row(**add_data)
  #add user to balances table
  print(f"new user {user_info[1]} added")
  return 0


@anvil.server.callable
def business_login(inp_username, inp_password):
  user = app_tables.business_data.get(username=inp_username)
  if user['password'] == inp_password:
    return user['businessID']
  else:
    return None


@anvil.server.callable
def user_login(inp_username, inp_password):
  user = app_tables.user_data.get(username=inp_username)
  if user['password'] == inp_password:
    return user['userID']
  else:
    return None


@anvil.server.callable
def add_funds(user_id, business_id, amount):
  row = dict(app_tables.balances.get(business=business_id))
  if row is None:
    return -1
  bal = row['user_data'].get(str(user_id))
  if bal is not None:
    bal += amount
  else:
    bal = amount
  row['user_data'][str(user_id)] = bal
  print(row['user_data'])
  app_tables.balances.get(business=business_id).update(user_data=row['user_data'])
  return row['user_data'][str(user_id)]

@anvil.server.callable
def add_funds_phone(phone_num, business_id, amount):
  user = app_tables.user_data.get(phone=phone_num)
  if user['userID'] is not None:
    return add_funds(user['userID'], business_id, amount)
  else:
    return -1

def add_funds_username(username_inp, business_id, amount):
  user = app_tables.user_data.get(username=username_inp)
  if user['userID'] is not None:
    return add_funds(user['userID'], business_id, amount)
  else:
    return -1

@anvil.server.callable
def make_purchace(user_id, business_id, amount_owed):
  row = dict(app_tables.balances.get(business=business_id))
  if row is None:
    return -1
  bal = row['user_data'].get(str(user_id))
  if bal is None:
    return amount_owed, 0
  elif bal > amount_owed:
    bal -= amount_owed
    amount_owed = 0
    row['user_data'][str(user_id)] = bal
  else:
    amount_owed -= bal
    bal = 0
    row['user_data'].pop(str(user_id))
  app_tables.balances.get(business=business_id).update(user_data=row['user_data'])
  return amount_owed, bal
  

@anvil.server.callable
def get_user_info(user_id):
  row = app_tables.user_data.get(userID=user_id)
  if row:
      # Convert row values to a list
      r = [value for value in row]
      r = [r[2][1], r[4][1], r[1][1]]
      return r
  else:
      print("Row not found.")
      return None
    

@anvil.server.callable
def get_business_info(business_id):
  row = app_tables.business_data.get(businessID=business_id)
  if row:
      # Convert row values to a list
      r = [value for value in row]
      r = [r[0][1], r[2][1]]
      return r
  else:
      print("Row not found.")
      return None


@anvil.server.callable
def add_unlinked(business_id, value):
  add_data = {}
  user_id = randrange(1000000000000000,9999999999999999)
  #check if user_id is already assigned to another user
  while app_tables.unlinked.get(unlinkedID=user_id) is not None:
    user_id = randrange(1000000000000000,9999999999999999)
  add_data['unlinkedID'] = user_id
  add_data['value'] = value
  add_data['businessID'] = business_id
  print(add_data['value'])
  app_tables.unlinked.add_row(**add_data)
  return user_id

@anvil.server.callable
def claim_unlinked(unlinked_id,user_id):
  row = dict(app_tables.unlinked.get(unlinkedID=unlinked_id))
  add_funds(user_id, row['businessID'],row['value'])
  app_tables.unlinked.get(unlinkedID=unlinked_id).delete()
  


# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
# In your server module (e.g., ServerFunctions)

import anvil.tables as tables
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def add_business(business_info):
    business_name, business_username, business_password = business_info

    # Check if a business with this username already exists
    existing_business = app_tables.businesses.get(username=business_username)
    if existing_business:
        return -1  # Username already exists

    # Add the business to the database
    app_tables.businesses.add_row(
        name=business_name,
        username=business_username,
        password=business_password
    )
    return 0  # Success
  
import anvil.server
import anvil.tables as tables
from anvil.tables import app_tables

@anvil.server.callable
def get_all_businesses():
    # Retrieve all businesses and return relevant fields as a list of dictionaries
    return [
        {
            "name": business["name"],
        }
        for business in app_tables.businesses.search()
    ]
class GiftCardSystem:
    def __init__(self):
        # Simulated databases
    businesses = {}  # Key: business_username, Value: [business_name, business_password, business_id]
    users = {}       # Key: user_username, Value: [user_name, user_password, user_phone, user_id]
    balances = {}    # Key: (user_id, business_id), Value: balance
  
import anvil.server

@anvil.server.callable
def add_business(business_info):
    """
    Adds a new business to the database.
    """
    name, username, password = business_info
    if username in businesses:
        return -1  # Username already exists
    business_id = generate_id()
    businesses[username] = [name, password, business_id]
    return 0  # Successful
  
import anvil.server

@anvil.server.callable
def add_user(user_info):
    """
    Adds a new user to the database.
    """
    name, username, password, phone = user_info
    if username in users:
        return -1  # Username already exists
    user_id = generate_id()
    users[username] = [name, password, phone, user_id]
    return 0  # Successful

import anvil.server

@anvil.server.callable
def business_login(input_username, input_password):
    """
    Logs in a business and returns its business ID if successful.
    """
    if input_username in businesses:
        _, stored_password, business_id = businesses[input_username]
        if input_password == stored_password:
            return business_id
    return None  # Login failed

import anvil.server

@anvil.server.callable
def user_login(input_username, input_password):
    """
    Logs in a user and returns its user ID if successful.
    """
    if input_username in users:
        _, stored_password, _, user_id = users[input_username]
        if input_password == stored_password:
            return user_id
    return None  # Login failed

import anvil.server

@anvil.server.callable
def add_funds(user_id, business_id, amount):
    """
    Adds funds to a user's balance for a specific business.
    """
    if not any(business_id in business[2] for business in businesses.values()):
        return -1  # Business does not exist
    balance_key = (user_id, business_id)
    current_balance = balances.get(balance_key, 0)
    balances[balance_key] = current_balance + amount
    return balances[balance_key]  # New balance


import anvil.server

@anvil.server.callable
def add_funds_phone(phone_num, business_id, amount):
    """
    Adds funds to a user by phone number.
    """
    for user in users.values():
        if user[2] == phone_num:  # Check phone number
            user_id = user[3]  # Retrieve user_id
            return add_funds(user_id, business_id, amount)
    return -1  # User not found

import anvil.server

@anvil.server.callable
def add_funds_username(username_inp, business_id, amount):
    """
    Adds funds to a user by username.
    """
    if username_inp in users:
        user_id = users[username_inp][3]  # Retrieve user_id
        return add_funds(user_id, business_id, amount)
    return -1  # User not found

import anvil.server

@anvil.server.callable
def make_purchase(user_id, business_id, amount_owed):
    """
    Deducts a purchase amount from a user's balance.
    """
    if not any(business_id in business[2] for business in businesses.values()):
        return -1  # Business does not exist
    balance_key = (user_id, business_id)
    current_balance = balances.get(balance_key, 0)
    if current_balance >= amount_owed:
        balances[balance_key] = current_balance - amount_owed
        return 0, balances[balance_key]  # Purchase successful
    else:
        return amount_owed - current_balance, 0  # Outstanding balance

import anvil.server

@anvil.server.callable
def get_user_info(user_id):
    """
    Retrieves user information.
    """
    for user in users.values():
        if user[3] == user_id:  # Match user_id
            return user[:3]  # [username, name, phone]
    return None  # User not found


import anvil.server

@anvil.server.callable
def get_business_info(business_id):
    """
    Retrieves business information.
    """
    for business in businesses.values():
        if business[2] == business_id:  # Match business_id
            return business[:2]  # [username, name]
    return None  # Business not found
