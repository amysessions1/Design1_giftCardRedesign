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
        }
        for business in app_tables.businesses.search()
    ]
class GiftCardSystem:
    def __init__(self):
        self.users = {}  # user_id: [username, password, phone_number, name]
        self.businesses = {}  # business_id: [username, password, name]
        self.user_balances = {}  # (user_id, business_id): balance

    def add_business(self, business_info):
        business_name, business_username, business_password = business_info
        if business_username in [b[0] for b in self.businesses.values()]:
            return -1  # Username already exists
        business_id = str(len(self.businesses) + 1).zfill(16)
        self.businesses[business_id] = [business_username, business_password, business_name]
        return 0  # Success

    def add_user(self, user_info):
        user_name, user_username, user_password, user_phone_number = user_info
        if user_username in [u[0] for u in self.users.values()]:
            return -1  # Username already exists
        user_id = str(len(self.users) + 1).zfill(16)
        self.users[user_id] = [user_username, user_password, user_phone_number, user_name]
        return 0  # Success

    def business_login(self, input_username, input_password):
        for business_id, (username, password, _) in self.businesses.items():
            if username == input_username and password == input_password:
                return business_id  # Login success, return business_id
        return None  # Incorrect username or password

    def user_login(self, input_username, input_password):
        for user_id, (username, password, _, _) in self.users.items():
            if username == input_username and password == input_password:
                return user_id  # Login success, return user_id
        return None  # Incorrect username or password

    def add_funds(self, user_id, business_id, amount):
        if business_id not in self.businesses:
            return -1  # Business does not exist
        if (user_id, business_id) not in self.user_balances:
            self.user_balances[(user_id, business_id)] = 0
        self.user_balances[(user_id, business_id)] += amount
        return self.user_balances[(user_id, business_id)]  # New balance

    def add_funds_phone(self, phone_num, business_id, amount):
        user_id = self.get_user_id_by_phone(phone_num)
        if user_id is None:
            return -1  # User not found
        return self.add_funds(user_id, business_id, amount)

    def add_funds_username(self, username_inp, business_id, amount):
        user_id = self.get_user_id_by_username(username_inp)
        if user_id is None:
            return -1  # User not found
        return self.add_funds(user_id, business_id, amount)

    def make_purchase(self, user_id, business_id, amount_owed):
        if business_id not in self.businesses:
            return -1  # Business does not exist
        current_balance = self.user_balances.get((user_id, business_id), 0)
        if current_balance < amount_owed:
            return amount_owed, current_balance  # Return remaining amount and card balance
        else:
            self.user_balances[(user_id, business_id)] -= amount_owed
            return 0, self.user_balances[(user_id, business_id)]  # Purchase complete, remaining balance

    def get_user_info(self, user_id):
        user_info = self.users.get(user_id)
        if user_info:
            return user_info  # [username, name, phone_number]
        return None  # User not found

    def get_business_info(self, business_id):
        business_info = self.businesses.get(business_id)
        if business_info:
            return business_info  # [username, name]
        return None  # Business not found

    def get_user_id_by_phone(self, phone_num):
        for user_id, (_, _, phone, _) in self.users.items():
            if phone == phone_num:
                return user_id
        return None  # User not found by phone number

    def get_user_id_by_username(self, username_inp):
        for user_id, (username, _, _, _) in self.users.items():
            if username == username_inp:
                return user_id
        return None  # User not found by username


