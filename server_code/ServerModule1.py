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
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
@anvil.server.callable
def add_business(business_info):
  #business_info should be a list of info in the form [{business name}, {business_username}, {business_password}] all as strings
  
  #generate business_id
  business_id = randrange(1000000000000000,9999999999999999)
  #add business to business_data table
  add_data = []
  add_data.append(business_id)
  for i in range(3):
    add_data.append(business_info[i])
  app_tables.business_data.add_row(add_data)
  #add business to balances table
  #add business to unlinked_balances