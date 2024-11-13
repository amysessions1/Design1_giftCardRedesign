import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

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
            "username": business["username"],
            "password": business["password"]
        }
        for business in app_tables.businesses.search()
    ]

