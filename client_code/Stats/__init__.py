from ._anvil_designer import StatsTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
#import pymysql
#from ._anvil_designer import ReportsTemplate

class Stats(StatsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Call a function to load and display stats
    self.load_stats()

  def load_stats(self):
    try:
      # Call the server function to get the statistics
      print("About to call the VSCode")
      total_images, potholes_detected = anvil.server.call('get_stats')
      print("returning from VSCOde")
  
      # Validate the values
      if total_images is not None and potholes_detected is not None:
          # Calculate potholes not detected
          potholes_not_detected = total_images - potholes_detected
  
          #Print debug information
          print(f"total images processed: {total_images}")
          print(f"total potholes detected: {potholes_detected}")
          print(f"total not potholes detected: {potholes_not_detected}")

          # Display the total number of images processed & Number of potholes detected 
          self.label_feedback_count.text = total_images
          self.label_detected_count.text = potholes_detected
        
          # Update the pie chart with the retrieved data
          self.plot_pie.data = [
              go.Pie(
                  labels=["Potholes Detected", "Potholes Not Detected"],
                  values=[potholes_detected, potholes_not_detected]
              )
          ]
      else:
        alert("Failed to load statistics or invalid data format.")
    except Exception as e:
      # Handle the case where the server call fails or returns unexpected data
      alert(f"Error loading statistics: {str(e)}")

