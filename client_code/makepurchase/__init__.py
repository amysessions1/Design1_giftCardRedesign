from ._anvil_designer import makepurchaseTemplate
from anvil import *
import anvil.server


class makepurchase(makepurchaseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  
  def text_box_1_pressed_enter(self, **event_args):
      """This method is called when the user presses Enter in this text box"""
      pass