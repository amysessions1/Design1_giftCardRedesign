from ._anvil_designer import Form1Template
from anvil import *
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
