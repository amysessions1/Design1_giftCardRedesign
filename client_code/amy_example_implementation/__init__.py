from ._anvil_designer import amy_example_implementationTemplate
from anvil import *
import anvil.server


class amy_example_implementation(amy_example_implementationTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def ex_add_business(self, **event_args):
    """Example of adding a business"""
    business_id = ["APPLE", "apple_company", "password"]
    anvil.server.call("add_business",business_id)

  def ex_add_user(self, **event_args):
    """Example of adding a business"""
    user_id = ["Billy Joel", "pianoMan1234", "password", "3098675309"]
    anvil.server.call("add_user",user_id)