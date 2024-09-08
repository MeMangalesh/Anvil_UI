import anvil.server
###########ADDED FOR STATS##########
import plotly.graph_objects as plt
import anvil.plotly_templates
anvil.plotly_templates.set_default("rally")
###########ADDED FOR STATS##########

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:

# Add new row into table
@anvil.server.callable
def get_data():
    return anvil.server.call('get_data')  # Call the VSCode uplink function
  
@anvil.server.callable
def save_image(image_base64, filename):
    # The call to Uplink function
    # return anvil.server.call('save_image', image_base64, filename)
    return anvil.server.call('save_image_n_trigger_detection', image_base64, filename)

@anvil.server.callable
def detect_potholes(image_base64, filename):
   # The call to Uplink function
   # Call the function in your VSCode environment that runs the YOLO model
   # return anvil.server.call('detect_potholes', image_base64, filename)
  try:
        pothole_detected, potholes_count = anvil.server.call('detect_potholes', image_base64, filename)
        return pothole_detected, potholes_count
  except Exception as e:
        # Handle any errors during the call
        return None

##############
## CODE FOR SAVING & TRIGGERING DETECTION
##############
@anvil.server.callable
def save_image_n_trigger_detection(self, image_base64, filename):
# Call the Anvil server function to detect potholes using the image ID
  result = anvil.server.call('detect_potholes', id) 
    # Unpack and display the result
  if result:
      pothole_detected, potholes_count, processed_image_base64 = result
      self.label_status.text = f"Potholes detected: {potholes_count}"
      self.image_detection.source = f"data:image/png;base64,{processed_image_base64}"
  else:
      self.label_status.text = "No potholes detected."
  
@anvil.server.callable
def detect_potholes_with_ID (self, id):
  # Call the Anvil server function to detect potholes using the image ID
  result = anvil.server.call('detect_potholes', image_id)
  
  # Unpack and display the result
  if result:
      pothole_detected, potholes_count, processed_image_base64 = result
      self.label_status.text = f"Potholes detected: {potholes_count}"
      self.image_detection.source = f"data:image/png;base64,{processed_image_base64}"
  else:
      self.label_status.text = "No potholes detected."

###########
###STATISTICS
############

def get_stats(self):
    # Fetch data from the server
      response = anvil.server.call('get_statistics')
      # print(response)  # Debugging: Print the response to check the data - print OK