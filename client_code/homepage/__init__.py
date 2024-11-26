from ._anvil_designer import homepageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..addbusiness import addbusiness
from ..adduser import adduser
from ..businesslogin import businesslogin
from ..userlogin import userlogin
from ..makepurchase import makepurchase
from ..addfunds import addfunds
from ..getuserinfo import getuserinfo


class homepage(homepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def add_business_click(self, **event_args):
    alert(
      content=addbusiness(),
      title="Edit Cards",
      large=True,
    )
  def add_user_click(self, **event_args):
    alert(
      content=adduser(),
      title="Add User",
      large=True,
    )

  def business_login_click(self, **event_args):
    alert(
      content=businesslogin(),
      title="Business Login",
      large=True,
    )
    
  def user_login_click(self, **event_args):
    alert(
      content=userlogin(),
      title="User Login",
      large=True,
    )

  def make_purchase_click(self, **event_args):
    alert(
      content=makepurchase(),
      title="Make Purchase",
      large=True,
    )

  def add_funds_click(self, **event_args):
    alert(
      content=addfunds(),
      title="Add Funds",
      large=True,
    )

  def get_user_info_click(self, **event_args):
    alert(
      content=getuserinfo(),
      title="Get User Info",
      large=True,
    )

  def demo_click(self, **event_args):
    """This method is called when the button is clicked"""
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
    print(user, comp)
    anvil.server.call('add_funds', user, comp, 10)
    anvil.server.call('add_funds', user, comp, 15)

    print(anvil.server.call('make_purchace', user, comp, 10))
    print(anvil.server.call('make_purchace', user, comp, 20))
    print(anvil.server.call('make_purchace', user, comp, 20))

    print(anvil.server.call('get_user_info', user))
    print(anvil.server.call('get_business_info', comp))

    x = anvil.server.call('add_unlinked', comp, 20)

    anvil.server.call('claim_unlinked', x, user)

  def user_funds_click(self, **event_args):
    open_form('balances_table')




    
    
    
