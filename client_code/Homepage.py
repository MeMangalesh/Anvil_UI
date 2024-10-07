from ._anvil_designer import HomepageTemplate
from anvil import *
# import anvil.server
#from Layout_copy import Layout_copy
from Layout import Layout
import Admin  # Absolute import for Admin
import Stats  # Absolute import for Stats
import Review  # Absolute import for Review
import Form1  # Absolute import for Form1
# import Form1_copy  # Absolute import for Form1

# Homepage Class Definition
class Homepage(HomepageTemplate):  # Your landing page form
  def __init__(self, **properties):
    self.init_components(**properties)
    # self.banner.role = ['spaced-title', 'left-right-padding']

  # Any code you write here will run before the form opens.
    for button in [self.button_admin, self.button_dashboard, self.button_demo, self.button_review]:
      button.role = ['spaced-title', 'display-none-responsive']
  
  def button_demo_click(self, **event_args):
  # Create an instance of the Layout form
    layout_form = Layout()
    # Load Formtest into the content slot of Layout
    # layout_form.load_child_form(Form1_copy.Form1_copy())
    layout_form.load_child_form(Form1.Form1())
    # Open the Layout form
    open_form(layout_form)

  def button_admin_click(self, **event_args):
    # Load AdminForm into Layout
    layout_form = Layout()  # Create an instance of the Layout form
    layout_form.load_child_form(Admin.Admin())  # Load AdminForm into the content slot
    open_form(layout_form)  # Open the Layout form

  def button_dashboard_click(self, **event_args):
    # Load DashboardForm into Layout
    layout_form = Layout()  # Create an instance of the Layout form
    layout_form.load_child_form(Stats.Stats())  # Load DashboardForm into the content slot
    open_form(layout_form)  # Open the Layout form

  def button_review_click(self, **event_args):
    layout_form = Layout()
    layout_form.load_child_form(Review.Review())  
    open_form(layout_form)

  # def link_demo_homepg_click(self, **event_args):
  #   # Create an instance of the Layout form
  #   layout_form = Layout()
  #   # Load Form1 into the content slot of Layout
  #   layout_form.load_child_form(Form1())
  #   # Open the Layout form
  #   open_form(layout_form)



