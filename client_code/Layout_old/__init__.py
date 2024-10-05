from ._anvil_designer import Layout_oldTemplate
from anvil import *

# Import child forms that you plan to load into Layout
#from ..Homepage import Homepage  # Absolute import for Homepage
from ..Admin import Admin  # Absolute import for Admin
from ..Stats import Stats  # Absolute import for Stats
from ..Review import Review  # Absolute import for Review
from ..Form1 import Form1  # Absolute import for Form1

class Layout_old(Layout_oldTemplate):
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

  # def navigate(self, active_link, form):
  #     for i in [self.link_admin, self.link_dashboard, self.link_demo, self.link_review]:
  #       i.foreground = 'theme:Primary 700'
  #     active_link.foreground = 'theme:Secondary 500'
  #     self.column_panel_1.clear()
  #     self.column_panel_1.add_component(form, full_width_row=True)

  # Function to load child forms dynamically
  def load_child_form(self, form_instance):
    """Clear and load the selected form into the content slot."""
    # self.slot_content.clear()  # Clear any previous content in the slot
    # self.slot_content.add_component(form_instance)  # Add the new form to the slot
    self.column_panel_1.clear()  # Clear any previous content in the slot
    self.column_panel_1.add_component(form_instance)  # Add the new form to the slot

  # Function to load child forms dynamically
  def load_child_form(self, form_instance):
    self.column_panel_1.clear() # Clear any previous content in the slot
    self.column_panel_1.add_component(form_instance)  # Add the new form

  #  Load Demo form into Layout
  def link_demo_click(self, **event_args):
    layout_form = Layout()  # Create an instance of the Layout form
    layout_form.load_child_form(Form1())  # Load DashboardForm into the content slot
    open_form(layout_form)  # Open the Layout form

  #  Load Admin form into Layout
  def link_admin_click(self, **event_args):
    layout_form = Layout()  # Create an instance of the Layout form
    layout_form.load_child_form(Admin())  # Load DashboardForm into the content slot
    open_form(layout_form)  # Open the Layout form

  #  Load Admin form into Layout
  def link_review_click(self, **event_args):
    layout_form = Layout()  # Create an instance of the Layout form
    layout_form.load_child_form(Review())  # Load DashboardForm into the content slot
    open_form(layout_form)  # Open the Layout form

  #  Load Admin form into Layout
  def link_dashboard_click(self, **event_args):
    layout_form = Layout()  # Create an instance of the Layout form
    layout_form.load_child_form(Stats())  # Load DashboardForm into the content slot
    open_form(layout_form)  # Open the Layout form