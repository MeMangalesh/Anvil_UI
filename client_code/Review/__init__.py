from ._anvil_designer import ReviewTemplate
from anvil import *
import anvil.server
import datetime  # Import the datetime module

class Review(ReviewTemplate):
  def __init__(self, **properties):
    # Any code you write here will run before the form opens.
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
     # Set max_date to today's date for both date pickers
    today = datetime.date.today()  # Get today's date using datetime
    self.date_picker_from.max_date = today  # Restrict 'from' date picker to today's date
    self.date_picker_to.max_date = today    # Restrict 'to' date picker to today's date
        
    # Call the method to load images
    self.load_undetected_images()
    
#####
# Filter records by processed date
#####

  def button_view_click(self, **event_args):
    date_from = self.date_picker_from.date  # Access the date property
    date_to = self.date_picker_to.date  # Access the date property
  
    # Validation: Ensure 'from' date is not greater than 'to' date
    if date_from > date_to:
      alert("The 'From' date must be before or the same as the 'To' date. Please select a valid date range.", title="Invalid Date Range")
    else:
      # If valid, proceed to load images by the selected date range
      self.load_undetected_images_by_date(date_from, date_to)
  
  def load_undetected_images_by_date(self, date_from, date_to):
    try:
        # Call the server function to get images
        print("Inside the load_undetected_images_by_date function in Anvil Form")
        image_data_list = anvil.server.call('get_data_by_date', date_from, date_to)
  
        # Check the status of the response
        if image_data_list['status'] == 'success':
          # Set the repeating panel with the list of image data
          self.repeating_panel_1.items = image_data_list['data']
        else:
            # Handle errors, e.g., show an alert
            alert(image_data_list['message'])
    except Exception as e:
        alert(f"An error occurred: {e}")

####
# End of Filter records by processed date
#####


  #####
  ##Code below is working fine without date filter
  #####
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




