from ._anvil_designer import HomepageTemplate
from anvil import *
import anvil.server

# Explicitly import forms
from App import Layout, Demo, Admin, Dashboard, Review  # Replace 'your_module_name' with the actual module name where your forms are defined

# Homepage Class Definition
class Homepage(HomepageTemplate):  # Your landing page form
    def __init__(self, **properties):
        self.init_components(**properties)

    def button_demo_click(self, **event_args):
        # Load DemoForm into Layout
        layout_form = Layout()  # Create an instance of the Layout form
        layout_form.load_child_form(Demo())  # Load DemoForm into the content slot
        open_form(layout_form)  # Open the Layout form

    def button_admin_click(self, **event_args):
        # Load AdminForm into Layout
        layout_form = Layout()  # Create an instance of the Layout form
        layout_form.load_child_form(Admin())  # Load AdminForm into the content slot
        open_form(layout_form)  # Open the Layout form

    def button_dashboard_click(self, **event_args):
        # Load DashboardForm into Layout
        layout_form = Layout()  # Create an instance of the Layout form
        layout_form.load_child_form(DashboardForm())  # Load DashboardForm into the content slot
        open_form(layout_form)  # Open the Layout form

    def button_review_click(self, **event_args):
        # Load ReviewForm into Layout
        layout_form = Layout()  # Create an instance of the Layout form
       
