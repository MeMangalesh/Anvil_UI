from ._anvil_designer import Form1Template
from anvil import *
import anvil.server  # Ensure server module is imported
import base64

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_submit_click(self, **event_args):
    result = anvil.server.call('say_hello', 'Anvil User')
   # Notification("Feedback submitted!").show()
    alert(result)  # This should display "Hello, Anvil User from FastAPI!"

  def file_loader_1_change(self, file, **event_args):
   # Display this file in an Image component
    self.image_byuser.source = file
  
  def button_upload_img_click(self, **event_args):
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
          self.label_status.text = "Image uploaded and saved successfully!"
      else:
          self.label_status.text = f"Failed to save image: {result['message']}"
    else:
      self.label_status.text = "No file selected."

  def button_detect_click(self, **event_args):
      # Assuming the image has already been uploaded and saved,
      # now call the YOLO model to detect potholes
      file = self.file_loader_1.file
      if file:
          filename = file.name
          file_data = file.get_bytes()

          # Encode the file in base64
          encoded_image = base64.b64encode(file_data).decode('utf-8')
          print("Image encoded for detection")

          # Call the Anvil server function to detect potholes
          result = anvil.server.call('detect_potholes', encoded_image, filename)
          
          # Unpack and display the result from the tuple 
          if result:
             # Display the processed image with bounding boxes
            pothole_detected, potholes_count = result  # Unpacking tuple/list
            self.label_status.text = f"Potholes detected: {potholes_count}"
            self.image_detection.source = f"data:image/png;base64,{result_image_base64}"
          else:
              self.label_status.text = "No potholes detected."
      else:
          self.label_status.text = "No file selected."
