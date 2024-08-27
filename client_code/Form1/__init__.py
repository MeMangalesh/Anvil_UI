from ._anvil_designer import Form1Template
from anvil import *
import anvil.server  # Ensure server module is imported

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_submit_click(self, **event_args):
    result = anvil.server.call('say_hello', 'Anvil User')
   # Notification("Feedback submitted!").show()
    alert(result)  # This should display "Hello, Anvil User from FastAPI!"

