from ._anvil_designer import LayoutTemplate
from anvil import *
import anvil.server

# Import child forms that you plan to load into Layout
import Formtest  # Import only the forms that you will use
from .Demo import Demo
from .Admin import Admin
from .Dashboard import Dashboard
from .Review import Review

class Layout(LayoutTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  # Any code you write here will run before the form opens.
  
  # Function to load child forms dynamically
  def load_child_form(self, form_instance):
    self.content_slot.clear()  # Clear any previous content in the slot
    self.content_slot.add_component(form_instance)  # Add the new form

  def link_dashboard_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass
