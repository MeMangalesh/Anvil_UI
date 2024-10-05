from ._anvil_designer import Layout_copyTemplate
from anvil import *
import anvil.server

# Import child forms that you plan to load into Layout
#from ..Homepage import Homepage  # Absolute import for Homepage
from ..Admin import Admin  # Absolute import for Admin
from ..Stats import Stats  # Absolute import for Stats
from ..Review import Review  # Absolute import for Review
from ..Form1 import Form1  # Absolute import for Form1

class Layout_copy(Layout_copyTemplate):
  def __init__(self, **properties):
      # Set Form properties and Data Bindings.
      self.init_components(**properties)
      # Load the default form (Homepage) when Layout_copy is first opened
      # self.load_child_form(Homepage.Homepage())  # Load Homepage initially
      
      # Any code you write here will run before the form opens.
      for link in [
          self.link_admin,
          self.link_dashboard,
          self.link_demo,
          self.link_review,
      ]:
          link.role = ["spaced-title", "display-none-responsive"]

  # Function to load child forms dynamically
  def load_child_form(self, form_instance):
      """Clear and load the selected form into the content slot."""
      # self.slot_content.clear()  # Clear any previous content in the slot
      # self.slot_content.add_component(form_instance)  # Add the new form to the slot
      self.column_panel_1.clear()  # Clear any previous content in the slot
      self.column_panel_1.add_component(form_instance)  # Add the new form to the slot

  # Event handler: Load Demo form into Layout
  def link_demo_click(self, **event_args):
      self.load_child_form(Form1())  # Load Demo form into the content slot

  # Event handler: Load Admin form into Layout
  def link_admin_click(self, **event_args):
      self.load_child_form(Admin())  # Load Admin form into the content slot

  # Event handler: Load Review form into Layout
  def link_review_click(self, **event_args):
      self.load_child_form(Review())  # Load Review form into the content slot

  # Event handler: Load Dashboard form into Layout
  def link_dashboard_click(self, **event_args):
      self.load_child_form(Stats())  # Load Dashboard (Stats) form into the content slot
