import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:

# Add new row into table
@anvil.server.callable
def display_data():
  # Dispaly records from the image_data table 
  return anvil.server.call('get_data')
  
@anvil.server.callable
def save_image(image_base64, filename):
    # The call to Uplink function
    return anvil.server.call('save_image', image_base64, filename)

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
def save_trigger_detection(image_base64, filename):
# Call the Anvil server function to detect potholes using the image ID
  result = anvil.server.call('detect_potholes', id)
  
 