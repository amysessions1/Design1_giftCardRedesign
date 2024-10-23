from ._anvil_designer import homepageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..cardedit import cardedit


class homepage(homepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def view_cards_click(self, **event_args):
    alert(
      content=cardedit(),
      title="Edit Cards",
      large=True,
    )
