from ._anvil_designer import HomepageTemplate
from anvil import *
# import anvil.server
# from Layout import Layout  # Import Layout

# Homepage Class Definition
class Homepage(HomepageTemplate):  # Your landing page form
  def __init__(self, **properties):
    self.init_components(**properties)
    # self.banner.role = ['spaced-title', 'left-right-padding']

  def button_demo_click(self, **event_args):
  # Create an instance of the Layout form
    layout_form = Layout()
    # Load Formtest into the content slot of Layout
    layout_form.load_child_form(Formtest())
    # Open the Layout form
    open_form(layout_form)

  def button_admin_click(self, **event_args):
    # Load AdminForm into Layout
    layout_form = Layout()  # Create an instance of the Layout form
    layout_form.load_child_form(Admin())  # Load AdminForm into the content slot
    open_form(layout_form)  # Open the Layout form

  def button_dashboard_click(self, **event_args):
    # Load DashboardForm into Layout
    layout_form = Layout()  # Create an instance of the Layout form
    layout_form.load_child_form(Stats())  # Load DashboardForm into the content slot
    open_form(layout_form)  # Open the Layout form

  def button_review_click(self, **event_args):
    layout_form = Layout()
    layout_form.load_child_form(Review())  
    open_form(layout_form)

  def link_demo_click(self, **event_args):
    # Create an instance of the Layout form
    layout_form = Layout()
    # Load Form1 into the content slot of Layout
    layout_form.load_child_form(Form1())
    # Open the Layout form
    open_form(layout_form)

  def link_test_click(self, **event_args):
    layout_form = Layout()
    layout_form.load_child_form(Formtest())  
    open_form(layout_form)

