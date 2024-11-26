from ._anvil_designer import balances_tableTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import globals

class balances_table(balances_tableTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.repeating_panel_1.items = app_tables.balances.search(user_data=globals.user_id)
    # Any code you write here will run before the form opens.
