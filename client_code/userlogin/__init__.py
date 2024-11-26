from ._anvil_designer import userloginTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from .. import globals


class userlogin(userloginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def submit_click(self, **event_args):
    username = self.user_name.text
    password = self.user_pw.text
    globals.user_id = anvil.server.call('user_login',username,password)
    print(globals.user_id)
