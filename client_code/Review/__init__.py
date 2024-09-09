from ._anvil_designer import ReviewTemplate
from anvil import *
import anvil.server

class Review(ReviewTemplate):
  def __init__(self, **properties):
    # Any code you write here will run before the form opens.
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Call the method to load images
    self.load_undetected_images()

  def load_undetected_images(self):
      try:
          # Call the server function to get images
          print("Inside the load_undetected_images function in Anvil Form")
          image_data_list = anvil.server.call('get_images')
  
          # Check the status of the response
          if image_data_list['status'] == 'success':
            # Set the repeating panel with the list of image data
            self.repeating_panel_1.items = image_data_list['data']
          else:
              # Handle errors, e.g., show an alert
              alert(image_data_list['message'])
      except Exception as e:
          alert(f"An error occurred: {e}")
  


