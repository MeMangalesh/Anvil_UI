from ._anvil_designer import AdminTemplate
from anvil import *
import anvil.server
import base64

class Admin(AdminTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  # Any code you write here will run before the form opens.
   # Fetch data from the server and set it to the repeating panel
    data = anvil.server.call('display_data')
    
    if data['status'] == 'success':
        self.repeating_panel_image_data.items = data['data']
    else:
        anvil.Notification("Failed to load data").show()
   
  def file_loader_1_change(self, file, **event_args):
   # Display this file in an Image component
    self.image_upload.source = file
    # self.button_activate(self)

  def button_save_click(self, **event_args):
     # Get the uploaded file from the FileLoader component
    file = self.file_loader_1.file
    if file:
      filename = file.name
      file_data = file.get_bytes()
      
      # Encode the file in base64
      encoded_image = base64.b64encode(file_data).decode('utf-8')
      print("image encoded")

      # Call the Anvil server function to save the image
      result = anvil.server.call('save_image', encoded_image, filename)
            
      # Display the result message
      if result['status'] == 'success':
          self.label_message.text = "Image uploaded and saved successfully!"
      else:
          self.label_message.text = f"Failed to save image: {result['message']}"
    else:
      self.label_message.text = "No file selected."
    
  # Deactivate the "Reset" button after saving 
  
  def outlined_button_reset_click(self, **event_args):
    # Clear the image displayed in the Image component
    self.image_upload.source = None 
    # # Clear the image displayed in the Image component
    # self.image_detection.source = None 
    # Clear the uploaded file from the file loader
    self.file_loader_1.clear()
   


