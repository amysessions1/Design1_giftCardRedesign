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




