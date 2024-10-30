from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server



class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def amy_testing_click(self, **event_args):
    """This method is called when the button is clicked"""
    business_id = ["APPLE", "apple_company", "password"]
    anvil.server.call("add_business",business_id)
    """This method is called when the button is clicked"""
    business_id = ["APPLE", "apple_company1", "password"]
    anvil.server.call("add_business",business_id)
    """This method is called when the button is clicked"""
    business_id = ["APPLE", "apple_company2", "password"]
    anvil.server.call("add_business",business_id)
    """This method is called when the button is clicked"""
    business_id = ["APPLE", "apple_company3", "password"]
    anvil.server.call("add_business",business_id)
    """Example of adding a user"""
    user_id = ["Billy Joel", "pianoMan1234", "password", "3098675309"]
    anvil.server.call("add_user",user_id)
    """Example of adding a user"""
    user_id = ["Billy Joel", "pianoMan12345", "password", "3098675309"]
    anvil.server.call("add_user",user_id)
    """Example of adding a user"""
    user_id = ["Billy Joel", "pianoMan12346", "password", "3098675309"]
    anvil.server.call("add_user",user_id)
    """Example of adding a user"""
    user_id = ["Billy Joel", "pianoMan12347", "password", "3098675309"]
    anvil.server.call("add_user",user_id)

    user = anvil.server.call("user_login", "pianoMan12345", "password")
    comp = anvil.server.call('business_login', "apple_company2", "password")

    anvil.server.call('add_funds', user, comp, 10.1)
    anvil.server.call('add_funds', user, comp, 10.5)
    user = anvil.server.call("user_login", "pianoMan12346", "password")
    comp = anvil.server.call('business_login', "apple_company2", "password")
    anvil.server.call('add_funds', user, comp, 10)
    anvil.server.call('add_funds', user, comp, 15)
    user = anvil.server.call("user_login", "pianoMan12347", "password")
    comp = anvil.server.call('business_login', "apple_company", "password")
    anvil.server.call('add_funds', user, comp, 10)
    anvil.server.call('add_funds', user, comp, 15)

    print(anvil.server.call('make_purchace', user, comp, 10))
    print(anvil.server.call('make_purchace', user, comp, 20))
    print(anvil.server.call('make_purchace', user, comp, 20))

    print(anvil.server.call('get_user_info', user))
    print(anvil.server.call('get_business_info', comp))


    



