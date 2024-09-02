from ._anvil_designer import Form1Template
from anvil import *
import anvil.server  # Ensure server module is imported
import base64

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
  
    # Any code you write here will run before the form opens.
    # "Reset" and "Detect" buttons are disabled when form initialized
    self.button_deactivate(self)
    
  # def button_submit_click(self, **event_args):
  #   result = anvil.server.call('say_hello', 'Anvil User')
  #  # Notification("Feedback submitted!").show()
  #   alert(result)  # This should display "Hello, Anvil User from FastAPI!"

  def button_deactivate (self, file, **event_args):
    # Deactivate button when form loads and after every "Detect" and "Reset" button click
    self.button_reset.enabled = False
    self.button_detect.enabled = False

  def button_activate (self, file, **event_args):
    # Activate button when form loads and after every "Detect" and "Reset" button click
    self.button_reset.enabled = True
    self.button_detect.enabled = True

  def file_loader_1_change(self, file, **event_args):
   # Display this file in an Image component
    self.image_byuser.source = file
    self.button_activate(self)
  
  def button_upload_img_click(self, **event_args):
   # Get the uploaded file from the FileLoader component
    file = self.file_loader_1.file
    if file:
      filename = file.name
      file_data = file.get_bytes()
      # Activate the "Detect" button 
      self.button_detect.enabled = True
      # Encode the file in base64
      encoded_image = base64.b64encode(file_data).decode('utf-8')
      print("image encoded")

      # Call the Anvil server function to save the image
      result = anvil.server.call('save_image', encoded_image, filename)
            
      # Display the result message
      if result['status'] == 'success':
          self.label_status.text = "Image uploaded and saved successfully!"
      else:
          self.label_status.text = f"Failed to save image: {result['message']}"
    else:
      self.label_status.text = "No file selected."

  def button_detect_click(self, **event_args):
      # Call the function from VSCode to perform inference on image
      file = self.file_loader_1.file
      if file:
          filename = file.name
          file_data = file.get_bytes()

          # Deactivate the "Rest" and "Detect" buttons 
          self.button_deactivate(self)
        
          # Encode the file in base64
          encoded_image = base64.b64encode(file_data).decode('utf-8')
          print("Image encoded for detection")

          # Call the Anvil server function to detect potholes
          result = anvil.server.call('detect_potholes', encoded_image, filename)
          
          # Unpack and display the result from the tuple 
          if result:
             # Unpack the tuple returned by detect_potholes
            pothole_detected, potholes_count, processed_image_base64 = result  # Unpacking tuple/list
            #Display the processed image with bounding boxes
            self.label_status.text = f"Potholes detected: {potholes_count}"
            self.image_detection.source = f"data:image/png;base64,{processed_image_base64}"
          else:
              self.label_status.text = "No potholes detected."
      else:
          self.label_status.text = "No file selected."

  def button_reset_click(self, **event_args):
    # Clear the image displayed in the Image component
    self.image_byuser.source = None 
    # Clear the image displayed in the Image component
    self.image_detection.source = None 
    # Clear the uploaded file from the file loader
    self.file_loader_1.clear()
    self.button_detect.enabled = False
