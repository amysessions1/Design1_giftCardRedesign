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


business_data = []
user_data = []
business_index = []
user_index = []
balances = []
unlinked_balances = []


@anvil.server.callable
def add_business(business_info):
  #business_info should be a list of info in the form [{business name}, {business_username}, {business_password}] all as strings
  
  #generate business_id
  business_id = randrange(1000000000000000,9999999999999999)
  #check if business_id is already assigned to another business
  while business_id in business_index:
    business_id = randrange(1000000000000000,9999999999999999)
  #add business to business_data
  add_data = [business_id, business_info[0], business_info[1], business_info[2]]
  business_data.append(add_data)
  #add business to business_index
  business_index.append(business_id)
  #add business to balances table
  balances.append([])
  #add business to unlinked_balances
  unlinked_balances.append([])

def add_user(user_info):
  #user_info should be a list of info in the form [{user name}, {user_username}, {user_password}, {phone}] all as strings
  
  #generate user_id
  user_id = randrange(1000000000000000,9999999999999999)
  #check if user_id is already assigned to another user
  while user_id in user_index:
    user_id = randrange(1000000000000000,9999999999999999)
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

