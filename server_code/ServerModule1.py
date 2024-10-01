import anvil.server
###########ADDED FOR STATS##########
import plotly.graph_objects as plt
import anvil.plotly_templates
import plotly.express as px
import pandas as pd
import anvil.media
import io
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
  #result = anvil.server.call('detect_potholes', id) 
  result = anvil.server.call('detect_potholescore',id)
    # Unpack and display the result
  if result:
      pothole_detected, potholes_count, processed_image_base64 = result
      self.label_status.text = f"Potholes detected: {potholes_count}"
      self.image_detection.source = f"data:image/png;base64,{processed_image_base64}"
  else:
      self.label_status.text = "No potholes detected."
    
####################################################
### Original Function to detect potholes with ID ###
####################################################
# @anvil.server.callable
# def detect_potholes_with_ID (self, id):
#   # Call the Anvil server function to detect potholes using the image ID
#   result = anvil.server.call('detect_potholes', image_id)
  
#   # Unpack and display the result
#   if result:
#       pothole_detected, potholes_count, processed_image_base64 = result
#       self.label_status.text = f"Potholes detected: {potholes_count}"
#       self.image_detection.source = f"data:image/png;base64,{processed_image_base64}"
#   else:
#       self.label_status.text = "No potholes detected."

####################################################
### Amended Function to detect potholes, score & area with ID ###
####################################################
@anvil.server.callable
def detect_potholescore (id):
  print("Inside Anvil detect_potholescore server module function")
  print(f"id passed into function is: {id}")
  # Call the Anvil server function to detect potholes using the image ID
  result = anvil.server.call('detect_potholescore_with_ID', id)
  return result
  
  # Unpack and display the result
  if result:
      print("results returned back into detect_potholes in Anvil")
      pothole_detected, potholes_count, max_conf_score, min_conf_score, max_pothole_area, min_pothole_area = result
      #label_status.text = f"Potholes detected: {potholes_count}"
      #self.image_detection.source = f"data:image/png;base64,{processed_image_base64}"
      print(f"{potholes_count} potholes detected with max conf score: {max_conf_score}, max pothole area: {max_pothole_area}")
  else:
      #self.label_status.text = "No potholes detected."
      print("No potholes detected")
  

###########
###STATISTICS
############
@anvil.server.callable
def fetch_min_max_dates(self):
    # Call the VSCode uplink function to get the min and max dates
    results = anvil.server.call('get_min_max_dates')
    return results     

#########
## Gauge Meter for Confidence Score 
#########
# Function to call the uplink code in VSCode
@anvil.server.callable
def fetch_avg_max_conf_score():
  avg_max_conf_score = anvil.server.call('get_avg_max_conf_score')
  return avg_max_conf_score

###################
## Bubble Chart 
###################
@anvil.server.callable
def get_pothole_bubble_data():
    try:
        # Call the VSCode function to get pothole bubble data
        result = anvil.server.call('get_pothole_bubble_data')

        if result['status'] == "success":
            return {
                "status": "success",
                "pothole_counts": result['pothole_counts'],
                "frequencies": result['frequencies'],
                "avg_conf_scores": result['avg_conf_scores']
            }
        else:
            return {"status": "error", "message": result['message']}
    
    except Exception as e:
        logging.error(f"An error occurred when calling the VSCode function: {e}")
        return {"status": "error", "message": str(e)}

@anvil.server.callable
def get_stats():
# Fetch data from the server
  pie_stats = anvil.server.call('get_statistics')
  print("Returned from vscode")

### SUMMARY FIGURE & PIE CHART ###
# Check if the call was successful
  print(f"Return status: {pie_stats['status']}")
  if pie_stats['status'] == 'success':
      # The `data` contains two values: total_images, potholes_detected
      total_images, potholes_detected = map(int, pie_stats['data'])  # Ensure all values are integers
      print(f"{total_images} & {potholes_detected}")
      # Ensure the data contains exactly two values
      try:
          total_images, potholes_detected = map(int, pie_stats['data'])  # Ensure all values are integers
          print(f"Total images: {total_images}, Potholes detected: {potholes_detected}")
          
          # Return the results in the required format
          return {
              "total_images": total_images,
              "potholes_detected": potholes_detected
          }
      except ValueError as e:
          print(f"Error unpacking data: {e}")
          return {"status": "error", "message": "Error unpacking data"}
  else:
      # Log the error message if the call fails
      print(pie_stats['message'])
      return {"status": "error", "message": pie_stats['message']}

### LINE CHART ####
@anvil.server.callable
def fetch_pothole_trends():
    result = anvil.server.call('get_pothole_trends')
    return result

### HEATMAP ####
@anvil.server.callable
def fetch_severity_heatmap():
  heatmap_data = anvil.server.call('get_severity_data')
  return heatmap_data

### BAR CHRAT ####
@anvil.server.callable
def fetch_severity_data():
  severity_data = anvil.server.call('get_severity_data')
  return severity_data

###################
## double line graph - feedbk, potholes detected vs. date
###################
@anvil.server.callable
def fetch_feedback_and_potholes():
    results = anvil.server.call('get_daily_feedback_and_potholes') 
    return results

#########################
### FILTER BY DATE #####
@anvil.server.callable
def fetch_data_by_date():
# Fetch data from the server
  pie_stats = anvil.server.call('get_data_by_range')
  #print(pie_stats)  # Debugging: Print the response to check the data - print OK

##############
##REVIEW DETECTION RESULT
###############
@anvil.server.callable
def get_images():
  #get the images from DB
  print("Calling vscode")
  result = anvil.server.call('get_images')
  
   # Unpack and display the result
  if result:
      self.label_status.text = "Results returned from VSCode query"
      # Return the result directly to the client
      return result['data']
  else:
      self.label_status.text = "No records exist."
      return {"status": "error", "message": "No records found"}

##########
## UPDATE REVIEW RESULTS
##########
@anvil.server.callable
def update_review(image_id):
  print("calling vscode to save image review result")
  result = anvil.server.call('save_review', image_id)

# Unpack and display the result
  if result:
      print("Review updated successfully")  # Optional: Log the result for debugging
      return {"status": "success", "message": "Review updated successfully"}
  else:
      return {"status": "error", "message": "No records found"}


  