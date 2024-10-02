from ._anvil_designer import Admin_oldTemplate
from anvil import *
import anvil.server
import base64
import anvil.media

class Admin_old(Admin_oldTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Load data when the form is initialized
    self.load_data()
    
  def file_loader_1_change(self, file, **event_args):
   # Display this file in an Image component
    self.image_upload.source = file
    # self.button_activate(self)

  def load_data(self):
    # Fetch data from the server
      response = anvil.server.call('get_data')
      # print(response)  # Debugging: Print the response to check the data - print OK

      # Check the status of the response
      if response['status'] == 'success':
          # Set the data to the RepeatingPanel
          self.repeating_panel_image_data.items = response['data']
      else:
          # Handle errors, e.g., show an alert
          alert(response['message'])
    
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

            # Call the Anvil server function to detect potholes
      result = anvil.server.call('detect_potholes', encoded_image, filename)
          
      # Unpack and display the result from the tuple 
      if result:
          # Unpack the tuple returned by detect_potholes
        pothole_detected, potholes_count, processed_image_base64 = result  # Unpacking tuple/list
        #Display the processed image with bounding boxes
        # self.label_status.text = f"Potholes detected: {potholes_count}"
        self.image_detection.source = f"data:image/png;base64,{processed_image_base64}"
      else:
          self.label_message.text = "No potholes detected."
    else:
        self.label_message.text = "No file selected."

    # Call the Anvil server function to save image with ID & detect potholes
    self.label_message.text = "Calling save_image_n_trigger_detection function"
    image_id = anvil.server.call("save_image_n_trigger_detection", encoded_image, filename)
  
    if image_id:
      self.label_message.text = f"Image uploaded successfully with ID {image_id}."
      # Now trigger pothole detection using the saved image ID
      self.trigger_pothole_detection(image_id)
    else:
      self.label_message.text = "Failed to save image."
      
  def trigger_pothole_detection(self, image_id):
      # Call the Anvil server function to detect potholes using the image ID
      #image_id = 83
      print(f"Image id: {image_id}")
      self.label_2.text = "Inside the trigger pothole function"
      #result = anvil.server.call("detect_potholes_with_ID", image_id)
      result = anvil.server.call("detect_potholescore", image_id)
      # Unpack and display the result
      if result:
        #pothole_detected, potholes_count, processed_image_base64 = result
        pothole_detected, potholes_count, max_conf_score, min_conf_score, max_pothole_area, min_pothole_area = result
        self.label_1.text = f"Potholes detected: {potholes_count}"
        #self.image_detection.source = f"data:image/png;base64,{processed_image_base64}"
      else:
        self.label_message.text = "No potholes detected."
  
  ## code below before merging w latest code from Admin copy ##
  # else:
  #   self.label_message.text = "No file selected."

    #   # Call the Anvil server function to save the image and get the ID
    #   self.label_message.text = "Calling save_image_n_trigger_detection function"
    #   image_id = anvil.server.call('save_image_n_trigger_detection', encoded_image, filename)
      
    #   if image_id:
    #       self.label_message.text = f"Image uploaded successfully with ID {image_id}."
    #       # Now trigger pothole detection using the saved image ID
    #       self.trigger_pothole_detection(image_id)
    #   else:
    #       self.label_message.text = "Failed to save image."
    # else:
    #   self.label_message.text = "No file selected."

  # def trigger_pothole_detection(self, image_id):
  #   # Call the Anvil server function to detect potholes using the image ID
  #   self.label_2.text = "Inside the trigger pothole function"
  #   result = anvil.server.call('detect_potholes_with_ID', image_id)
  
  #   # Unpack and display the result
  #   if result:
  #       pothole_detected, potholes_count, processed_image_base64 = result
  #       self.label_1.text = f"Potholes detected: {potholes_count}"
  #      # self.image_detection.source = f"data:image/png;base64,{processed_image_base64}"
  #   else:
  #       self.label_message.text = "No potholes detected."

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

  def button_reset_click(self, **event_args):
    # Clear the image displayed in the Image component
    self.image_byuser.source = None 
    # Clear the image displayed in the Image component
    self.image_detection.source = None 
    # Clear the uploaded file from the file loader
    self.file_loader_1.clear()
    self.button_detect.enabled = False
    self.label_status.text = None
  

  def link_User_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form1')

  def link_Dashboard_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Stats')

  def link_Review_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Review')

  def link_Admin_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Admin')

  def button_save_img_click(self, **event_args):
    # Get the uploaded file from the FileLoader component
    file = self.file_loader_1.file
    if file:
      filename = file.name
      file_data = file.get_bytes()
      # Activate the "Detect" button 
      # self.button_detect.enabled = True
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

 
   


