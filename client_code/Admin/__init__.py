from ._anvil_designer import AdminTemplate
from anvil import *
import anvil.server
import base64
import anvil.media

class Admin(AdminTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    #Initialize form with default 
    self.label_message.text = "Upload image to view detection result"
    self.button_deactivate(self)

  def file_loader_1_change(self, file, **event_args):
    # Display this file in an Image component
    self.image_upload.source = file
    self.button_activate(self) 

  def button_activate (self, file, **event_args):
    self.image_detection.source = None
    # Clear the uploaded file from the file loader
    #self.file_loader_1.clear()
    # self.label_1.text = None
    # self.label_2.text = None
    
    #self.message.text = self.init_components()
    self.outlined_button_reset.enabled = True
    self.button_save_n_detect.enabled = True
    self.file_loader_1.enabled = False

  def button_deactivate (self, file, **event_args):
    # Deactivate button when form loads and after every "Detect" and "Reset" button click
    # Clear the image displayed in the Image component
    #self.image_upload.source = None  --------------- commented this
    # Clear the image displayed in the Image component
    self.image_detection.source = None
    # Clear the uploaded file from the file loader
    self.file_loader_1.clear()
    self.label_1.text = None
    self.label_2.text = None
    
    self.label_message.text = self.init_components()
    self.outlined_button_reset.enabled = False
    self.button_save_n_detect.enabled = False
    self.file_loader_1.enabled = True

  def load_data(self):
    # Fetch data from the server
    response = anvil.server.call("get_data")
    
    # Check the status of the response
    if response["status"] == "success":
        # Sort the data in descending order based on a key (e.g., 'date')
        sorted_data = sorted(response["data"], key=lambda x: x['id'], reverse=True)
        # Set the sorted data to the RepeatingPanel
        self.repeating_panel_image_data.items = sorted_data
    else:
        # Handle errors, e.g., show an alert
        alert(response["message"])
 
    # # Toggle visibility of the DataGrid
    # self.data_grid_1.visible = not self.data_grid_1.visible
    # self.button_show_data.text = "HIDE DATA" if self.data_grid_1.visible else "SHOW DATA"
    
    # Check if the data grid is visible
    if not self.data_grid_1.visible:
        # If the DataGrid is hidden, show it and load data
        self.data_grid_1.visible = True
        self.load_data()  # Assuming you have a function to load the data
    #     # self.button_show_data.text = "HIDE DATA"  # Change button text to 'HIDE DATA'
    #     # self.button_show_data.visible = True      # Show the 'Hide Data' button below the DataGrid
    # else:
    #     # If the DataGrid is visible, hide it and reset the button
    #     self.data_grid_1.visible = False
    #     # self.button_show_data.text = "SHOW DATA"  # Change button text back to 'SHOW DATA'
    #     # self.button_show_data.visible = False 
  

  ##############
  ## Save image into DB & trigger detection with ID to detect, calculate score & update results into table
  ###############
  def button_save_n_detect_click(self, **event_args):
    file = self.file_loader_1.file
    if file:
      filename = file.name
      file_data = file.get_bytes()
      print(f"Filename: {filename}")
      #Deactivate button
      self.button_deactivate(self)

      # Encode the file in base64
      encoded_image = base64.b64encode(file_data).decode("utf-8")
      print("Image encoded for saving")

      # Call the Anvil server function to detect potholes
      result = anvil.server.call('detect_potholes', encoded_image, filename)

    else:
      self.label_message.text = "No file selected."
          
    # Unpack and display the result from the tuple 
    if result:
        # Unpack the tuple returned by detect_potholes
      pothole_detected, potholes_count, processed_image_base64 = result  # Unpacking tuple/list
      #Display the processed image with bounding boxes
      # self.label_status.text = f"Potholes detected: {potholes_count}"
      self.image_detection.source = f"data:image/png;base64,{processed_image_base64}"
      #self.label_message.text = "Potholes detected."
    else:
        self.label_message.text = "No potholes detected."
    # else:
    #     self.label_message.text = "No file selected."

    # Call the Anvil server function to save image with ID & detect potholes
    #self.label_message.text = "Calling save_image_n_trigger_detection function"
    image_id = anvil.server.call("save_image_n_trigger_detection", encoded_image, filename)
  
    if image_id:
      self.label_message.text = f"Image uploaded successfully with ID {image_id}."
      # Now trigger pothole detection using the saved image ID
      self.trigger_pothole_detection(image_id)
    else:
      self.label_message.text = "Failed to save image."
  

  ########
  ## Added text display effect 
    #########
  # Call this function to update the label based on detection results
  def update_message(self, potholes_detected):
    if potholes_detected:
        self.label_message.text = "Potholes Detected."
        self.label_result.foreground = "red"
        # self.timer_1.enabled = True  # Start blinking if potholes are detected
    else:
        self.label_result.text = "No potholes detected."
        self.label_result.foreground = "green"
        # self.timer_1.enabled = False  # No blinking for 'No potholes detected'
        self.label_result.visible = True  # Ensure text is visible in green
  
  # Timer event to make the text blink
  def timer_1_tick(self, **event_args):
    # Toggle visibility to create a blinking effect
    self.label_result.visible = not self.label_result.visible

  #########

  def trigger_pothole_detection(self, image_id):
    # Call the Anvil server function to detect potholes using the image ID
    #image_id = 83
    print(f"Image id: {image_id}")
    #self.label_2.text = "Inside the trigger pothole function"
    #result = anvil.server.call("detect_potholes_with_ID", image_id)
    result = anvil.server.call("detect_potholescore", image_id)
    # Unpack and display the result
    if result:
      #pothole_detected, potholes_count, processed_image_base64 = result
      pothole_detected, potholes_count, max_conf_score, min_conf_score, max_pothole_area, min_pothole_area = result
      self.label_result.text = "Potholes Detected."
      
      self.update_message(pothole_detected)
       
      self.label_1.text = f"{potholes_count}"
      self.label_2.text = f"{max_conf_score * 100:.2f}%"
      self.label_ID.text = f"{image_id}"
                 
      # self.image_detection.source = f"data:image/png;base64,{processed_image_base64}"
    else:
      self.label_result.text = "No potholes detected."

  #####################
  ## SHOW DETECTED IMAGE - 22092024
  #####################
  

  ##############
  ## END - Save image into DB & trigger detection using the newly created ID to fetch data, detect & update results back into DB
  ###############

  def outlined_button_reset_click(self, **event_args):
    # Clear the image displayed in the Image component
    self.image_upload.source = None
    # # Clear the image displayed in the Image component
    self.image_detection.source = None
    # Clear the uploaded file from the file loader
    self.file_loader_1.clear()
    # Enable the file upload button
    self.file_loader_1.enabled = True
    # Disable the save & detect button
    self.button_save_n_detect.enabled = False
    # self.label_status.text = None
   
  def link_User_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Form1")

  def link_Dashboard_click(self, **event_args):
    open_form("Stats")

  def link_Review_click(self, **event_args):
    open_form("Review")

  def link_Admin_click(self, **event_args):
    open_form("Admin")

  def button_show_data_click(self, **event_args):
    self.load_data()


    

  