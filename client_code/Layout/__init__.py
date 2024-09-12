from ._anvil_designer import LayoutTemplate
from anvil import *
import anvil.server

# Explicitly import forms
from App import Layout, Demo, Admin, Dashboard, Review  # Replace 'your_module_name' with the actual module name where your forms are defined

class Layout(LayoutTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  # Any code you write here will run before the form opens.
  
  # Function to load child forms dynamically
  def load_child_form(self, form_instance):
      self.content_slot.clear()  # Clear any previous content in the slot
      self.content_slot.add_component(form_instance)  # Add the new form
