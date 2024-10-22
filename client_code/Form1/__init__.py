from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def amy_testing_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.add_business(["APPLE", "apple_company", "password"])
