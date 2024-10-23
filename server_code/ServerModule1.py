import anvil.server
from random import randrange

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.


business_data = []
user_data = []
business_index = []
user_index = []
balances = []
unlinked_balances = []

@anvil.server.callable
def get_user_data():
  return user_data

@anvil.server.callable
def get_business_data():
  return business_data


@anvil.server.callable
def add_business(business_info):
  #business_info should be a list of info in the form [{business name}, {business_username}, {business_password}] all as strings
  #generate business_id
  business_id = randrange(1000000000000000,9999999999999999)
  #check if business_id is already assigned to another business
  while business_id in business_index:
    business_id = randrange(1000000000000000,9999999999999999)
  #check for unique username
  for i in business_data:
    if i[2] == business_info[1]:
      return -1
  #add business to business_data
  add_data = [business_id, business_info[0], business_info[1], business_info[2]]
  business_data.append(add_data)
  #add business to business_index
  business_index.append(business_id)
  #add business to balances table
  balances.append([])
  #add business to unlinked_balances
  unlinked_balances.append([])
  print("new business added")
  return 0


@anvil.server.callable
def add_user(user_info):
  #user_info should be a list of info in the form [{user name}, {user_username}, {user_password}, {phone}] all as strings
  #generate user_id
  user_id = randrange(1000000000000000,9999999999999999)
  #check if user_id is already assigned to another user
  while user_id in user_index:
    user_id = randrange(1000000000000000,9999999999999999)
  for i in user_data:
    if i[2] == user_info[1]:
      return -1
  #add user to user_data
  add_data = [user_id, user_info[0], user_info[1], user_info[2], user_info[3]]
  user_data.append(add_data)
  #add user to user_index
  user_index.append(user_id)
  #add user to balances table
  for i in range(len(business_index)):
    balances[i].append(0)
  #add user to unlinked_balances
    unlinked_balances[i].append(0)
  print("new user added")
  return 0


@anvil.server.callable
def business_login(inp_username, inp_password):
  j = business_data[1]
  print(j)
  for business in business_data:
    if business[2] == inp_username:
      if business[3] == inp_password:
        return business[0]
      else:
        return 1
    else:
      return -1


@anvil.server.callable
def user_login(inp_username, inp_password):
  print(user_data)
  for user in user_data:
    if user[2] == inp_username:
      if user[3] == inp_password:
        return user[0]
      else:
        return 1
    else:
      return -1
