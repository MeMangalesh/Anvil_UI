from ._anvil_designer import HomepageTemplate
from anvil import *
import anvil.server
# from .Layout import Layout  # Import Layout
# from .Formtest import Formtest  # Import Formtest

# Homepage Class Definition
class Homepage(HomepageTemplate):  # Your landing page form
  def __init__(self, **properties):
    self.init_components(**properties)
    
  def button_demo_click(self, **event_args):
    from .Layout import Layout
    from .Formtest import Formtest
    
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
