from ._anvil_designer import AdminTemplate
from anvil import *
import anvil.server
import base64
import anvil.media

class Admin(AdminTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  # Any code you write here will run before the form opens.
   # Fetch data from the server and set it to the repeating panel
    
  def file_loader_1_change(self, file, **event_args):
   # Display this file in an Image component
    self.image_upload.source = file
    # self.button_activate(self)

  ##############
  ## Code to save image
  ## Commented to try saving & using ID to fetch data, detect & update results back into DB
  ###############
  # def button_save_click(self, **event_args):
  #    # Get the uploaded file from the FileLoader component
  #   file = self.file_loader_1.file
  #   if file:
  #     filename = file.name
  #     file_data = file.get_bytes()
      
  #     # Encode the file in base64
  #     encoded_image = base64.b64encode(file_data).decode('utf-8')
  #     print("Image encoded and saved.")

  #     # Call the Anvil server function to save the image
  #     result = anvil.server.call('save_image', encoded_image, filename)
            
  #     # Display the result message
  #     if result['status'] == 'success':
  #         self.label_message.text = "Image uploaded and saved successfully!"
  #     else:
  #         self.label_message.text = f"Failed to save image: {result['message']}"
  #   else:
  #     self.label_message.text = "No file selected."
    
  # Deactivate the "Reset" button after saving 

  ##############
  ## START - Save image into DB & trigger detection using the newly created ID to fetch data, detect & update results back into DB
  ###############
  def button_save_n_detect_click(self, **event_args):
    file = self.file_loader_1.file
    if file:
      filename = file.name
      file_data = file.get_bytes()
      
      # Encode the file in base64
      encoded_image = base64.b64encode(file_data).decode('utf-8')
      print("Image encoded for saving")

      # Call the Anvil server function to save the image and get the ID
      self.label_message.text = "Calling save_image_n_trigger_detection function"
      image_id = anvil.server.call('save_image_n_trigger_detection', encoded_image, filename)
      
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
    result = anvil.server.call('detect_potholes_with_ID', image_id)
    
    # Unpack and display the result
    if result:
        pothole_detected, potholes_count, processed_image_base64 = result
        self.label_message.text = f"Potholes detected: {potholes_count}"
        self.image_detection.source = f"data:image/png;base64,{processed_image_base64}"
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

 
   


