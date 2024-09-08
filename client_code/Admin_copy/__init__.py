from ._anvil_designer import Admin_copyTemplate
from anvil import *
import anvil.server
import base64
import anvil.media


class Admin_copy(Admin_copyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Load data when the form is initialized
    self.load_data()
    self.date_from = None  # Initialize date_from
    self.date_to = None  # Initialize date_to

  def file_loader_1_change(self, file, **event_args):
    # Display this file in an Image component
    self.image_upload.source = file
    # self.button_activate(self)

  def load_data(self):
    # Fetch data from the server
    response = anvil.server.call("get_data")
    # print(response)  # Debugging: Print the response to check the data - print OK

    # Check the status of the response
    if response["status"] == "success":
      # Set the data to the RepeatingPanel
      self.repeating_panel_image_data.items = response["data"]
    else:
      # Handle errors, e.g., show an alert
      alert(response["message"])

  ##############
  ## START - Save image into DB & trigger detection using the newly created ID to fetch data, detect & update results back into DB
  ###############
  def button_save_n_detect_click(self, **event_args):
    file = self.file_loader_1.file
    if file:
      filename = file.name
      file_data = file.get_bytes()

      # Encode the file in base64
      encoded_image = base64.b64encode(file_data).decode("utf-8")
      print("Image encoded for saving")

      # Call the Anvil server function to save the image and get the ID
      self.label_message.text = "Calling save_image_n_trigger_detection function"
      image_id = anvil.server.call(
        "save_image_n_trigger_detection", encoded_image, filename
      )

      if image_id:
        self.label_message.text = f"Image uploaded successfully with ID {image_id}."
        # Now trigger pothole detection using the saved image ID
        self.trigger_pothole_detection(image_id)
      else:
        self.label_message.text = "Failed to save image."
    else:
      self.label_message.text = "No file selected."

  def trigger_pothole_detection(self, image_id):
    # Call the Anvil server function to detect potholes using the image ID
    self.label_2.text = "Inside the trigger pothole function"
    result = anvil.server.call("detect_potholes_with_ID", image_id)

    # Unpack and display the result
    if result:
      pothole_detected, potholes_count, processed_image_base64 = result
      self.label_1.text = f"Potholes detected: {potholes_count}"
    # self.image_detection.source = f"data:image/png;base64,{processed_image_base64}"
    else:
      self.label_message.text = "No potholes detected."

  #####################
  ## DETECTion TRIGGER
  #####################

  ##############
  ## END - Save image into DB & trigger detection using the newly created ID to fetch data, detect & update results back into DB
  ###############

  def outlined_button_reset_click(self, **event_args):
    # Clear the image displayed in the Image component
    self.image_upload.source = None
    # # Clear the image displayed in the Image component
    # self.image_detection.source = None
    # Clear the uploaded file from the file loader
    self.file_loader_1.clear()

  ##############
  ## STATS
  ##############

  def link_Dashboard_click(self, **event_args):
    #Clear the content panel and add the Reports Form
    self.content_panel.clear()
    self.content_panel.add_component(Stats())
    #Change the color of the sales_page_link to indicate that the Reports page has been selected
    self.reports_page_link.background = app.theme_colors['Primary Container']
    self.sales_page_link.background = "transparent"

  def button_show_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  class YourForm(YourFormTemplate):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.date_from = None  # Initialize date_from
    self.date_to = None  # Initialize date_to

  def date_picker_from_change(self, **event_args):
    """This method is called when the selected date changes"""
    self.date_from = self.date_picker_from.date
    self.call_server_function()

  def date_picker_to_change(self, **event_args):
    """This method is called when the selected date changes"""
    self.date_to = self.date_picker_to.date
    self.call_server_function()

  def call_server_function(self):
    """Call the server function with the selected dates"""
    # Handle cases where one of the dates might not be selected
    if self.date_from and not self.date_to:
      response = anvil.server.call('fetch_data_by_date', date_from=self.date_from)
    elif not self.date_from and self.date_to:
      response = anvil.server.call('fetch_data_by_date', date_to=self.date_to)
    elif self.date_from and self.date_to:
      response = anvil.server.call('fetch_data_by_date', date_from=self.date_from, date_to=self.date_to)
    else:
      # Both dates are not selected, do nothing or show a message
      return

    # Handle the response (e.g., update your UI)
    if response['status'] == 'success':
      # Update UI with the data received from the server
      pass
    else:
      # Handle the error
      alert(f"Error fetching data: {response['message']}")





