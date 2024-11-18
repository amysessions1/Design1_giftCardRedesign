from ._anvil_designer import businessloginTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class businesslogin(businessloginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)


  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    username = self.business_user.text
    password = self.business_pw.text
    anvil.server.session['id'] = anvil.server.call('business_login',username,password)
    print(anvil.server.session.get('id'))
    # Any code you write here will run before the form opens.
