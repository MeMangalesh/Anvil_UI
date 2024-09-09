from ._anvil_designer import ReviewTemplate
from anvil import *
import anvil.server

class Review(ReviewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

def load_undetected_images(self):
  # Call the server function to get images
    image_data_list = anvil.server.call('get_images')

  # Check the status of the response
    if image_data_list['status'] == 'success':
      # Set the repeating panel with the list of image data
      self.repeating_panel_1.items = image_data_list
    else:
        # Handle errors, e.g., show an alert
        alert(image_data_list['message'])

