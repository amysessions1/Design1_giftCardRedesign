from ._anvil_designer import addbusinessTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class addbusiness(addbusinessTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)

    def submit_button_click(self, **event_args):
        """This method is called when the user clicks the 'Submit' button to add a business."""
        
        # Retrieve values from input fields
        business_name = self.business_name.text
        business_username = self.business_username.text
        business_password = self.business_password.text

        # Check if fields are filled
        if not (business_name and business_username and business_password):
            alert("Please fill out all fields.")
            return

        # Call server function to add business
        result = anvil.server.call('add_business', [business_name, business_username, business_password])
        
        # Handle the result
        if result == 0:
            alert("Business added successfully!")
            self.clear_form()  # Optional: clear fields after successful submission
        elif result == -1:
            alert("Failed to add business: username already exists.")
    
    def clear_form(self):
        """Clears the input fields after successful submission."""
        self.business_name.text = ""
        self.business_username.text = ""
        self.business_password.text = ""
