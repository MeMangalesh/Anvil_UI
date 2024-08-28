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
    """This method is called when a new file is loaded into this FileLoader"""
    pass

  def button_upload_img_click(self, **event_args):
   # Get the uploaded file from the FileLoader component
    file = self.file_loader_1.file
    if file:
      filename = file.name
      file_data = file.get_bytes()

      # Encode the file in base64
      encoded_image = base64.b64encode(file_data).decode('utf-8')

      # Call the Anvil server function to save the image
      result = anvil.server.call('save_image', encoded_image, filename)
            
            # Display the result message
            if result['status'] == 'success':
                self.label_status.text = "Image uploaded and saved successfully!"
            else:
                self.label_status.text = "Failed to save image."
        else:

