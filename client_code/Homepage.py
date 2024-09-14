from ._anvil_designer import HomepageTemplate
from anvil import *
# import anvil.server
from Layout import Layout  # Import Layout

# from ..Formtest import Formtest  # Import only the forms that you will use
# from ..Admin import Admin
# from ..Admin.RowTemplate1 import RowTemplate1
# from ..Stats import Stats
# from ..Review import Review
# from ..Form1 import Form1

# Homepage Class Definition
class Homepage(HomepageTemplate):  # Your landing page form
  def __init__(self, **properties):
    self.init_components(**properties)
    # self.banner.role = ['spaced-title', 'left-right-padding']

  # Any code you write here will run before the form opens.
    for link in [self.link_admin_homepg, self.link_dashboard_homepg, self.link_demo_homepg, self.link_review_homepg]:
      link.role = ['spaced-title', 'display-none-responsive']
  
  def button_demo_click(self, **event_args):
  # Create an instance of the Layout form
    layout_form = Layout()
    # Load Formtest into the content slot of Layout
    layout_form.load_child_form(Form1())
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

  def link_demo_homepg_click(self, **event_args):
    # Create an instance of the Layout form
    layout_form = Layout()
    # Load Form1 into the content slot of Layout
    layout_form.load_child_form(Form1())
    # Open the Layout form
    open_form(layout_form)



