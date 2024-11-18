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




    
    
    
