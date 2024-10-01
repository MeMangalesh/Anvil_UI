from ._anvil_designer import ReviewTemplate
from anvil import *
import anvil.server
import datetime

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

    print(f"Start Date: {date_from}, End Date: {date_to}")
    
    # If no dates are selected, read all data in the database
    if not date_from and not date_to:
        # Load all data without date filter
        self.load_undetected_images_by_date(None, None)
    else:
        # Validation: Ensure 'from' date is not greater than 'to' date
        if date_from > date_to:
          alert("The 'From' date must be before or the same as the 'To' date. Please select a valid date range.", title="Invalid Date Range")
        else:
          # Proceed to load filtered images by the selected date range
          print("About to call load_undetected_images_by_date func in Anvil Review Form")
          self.load_undetected_images_by_date(date_from, date_to)

  
  def load_undetected_images_by_date(self, date_from, date_to):
    try:
        # Call the server function to get images
        print("Inside the load_undetected_images_by_date function in Anvil Form")
        print(f"Dates from: {date_from}")

      ###added below##
      # Ensure isinstance() is used correctly with proper types
        if isinstance(date_from, (datetime.datetime, datetime.date)):  # Check if date_from is a datetime or date type
          print(f"Dates from is valid: {date_from}")
        else:
            print(f"Invalid date_from: {date_from}")
        
        if isinstance(date_to, (datetime.datetime, datetime.date)):  # Check if date_to is a datetime or date type
            print(f"Dates to is valid: {date_to}")
        else:
            print(f"Invalid date_to: {date_to}")
        ### end added####
        image_data_list = anvil.server.call('get_data_by_date', date_from, date_to)
         
        # Debug: Print response from the server
        print(f"Response from server: {image_data_list}")
      
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





