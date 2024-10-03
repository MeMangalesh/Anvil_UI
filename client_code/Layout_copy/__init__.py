from ._anvil_designer import Layout_copyTemplate
from anvil import *
import anvil.server

# Import child forms that you plan to load into Layout
from ..Homepage import Homepage  # Import only the forms that you will use
from ..Admin import Admin

# from ..Admin.RowTemplate1 import RowTemplate1
from ..Stats import Stats
from ..Review import Review
from ..Form1 import Form1


class Layout_copy(Layout_copyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # self.navigate(self.column_panel_1, Homepage())

    # Any code you write here will run before the form opens.
    for link in [
      self.link_admin,
      self.link_dashboard,
      self.link_demo,
      self.link_review,
    ]:
      link.role = ["spaced-title", "display-none-responsive"]

  def navigate(self, active_link, form):
    for i in [self.link_admin, self.link_dashboard, self.link_demo, self.link_review]:
      i.foreground = "theme:Primary 700"
    active_link.foreground = "theme:Secondary 500"
    self.column_panel_1.clear()
    self.column_panel_1.add_component(form, full_width_row=True)
    
# ###Changed self.column_panel_1.clear() to self.slot_1.clear()
#   # Function to load child forms dynamically
#   def load_child_form(self, form_instance):
#     self.slot_1.clear()  # Clear any previous content in the slot
#     self.slot_1.add_component(form_instance)  # Add the new form
  
  # Function to load child forms dynamically
  def load_child_form(self, form_instance):
    self.slot_1.clear()  # Clear any previous content in the slot
    self.slot_1.add_component(form_instance)  # Add the new form
  
  # Load Demo form into Layout
  def link_demo_click(self, **event_args):
    layout_form = Layout()  # Create an instance of the Layout form
    layout_form.load_child_form(Form1())  # Load the Demo form into the content slot
    open_form(layout_form)  # Open the Layout form
  
  # Dynamically load different forms based on navigation choice (menu)
  def load_selected_form(self, form_name):
    layout_form = Layout()
    if form_name == "demo":
        layout_form.load_child_form(Form1())
    elif form_name == "dashboard":
        layout_form.load_child_form(Stats())
    elif form_name == "review":
        layout_form.load_child_form(Review())
    open_form(layout_form)

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
