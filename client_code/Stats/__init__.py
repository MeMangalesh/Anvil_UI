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
    # Call the server function to get the statistics
    stats = anvil.server.call('get_stats')

    # Debug: Print the entire stats structure
    print(f"Stats received: {stats}")

  # Check if stats were returned and ensure they are tuples
    if stats and isinstance(stats, tuple):
        total_images = stats[0][0]  # Extract the first element of the first tuple
        potholes_detected = stats[1][0]  # Extract the first element of the second tuple
        potholes_not_detected = total_images - potholes_detected
  
        # Print debug information
        print(f"total images processed: {total_images}")
        print(f"total potholes detected: {potholes_detected}")
        print(f"total not potholes detected: {potholes_not_detected}")
        
        # Update the pie chart with the retrieved data
        self.plot_pie.data = [
            go.Pie(
                labels=["Potholes Detected", "Potholes Not Detected"],
                values=[potholes_detected, potholes_not_detected]
            )
        ]
    else:
        alert("Failed to load statistics or invalid data format.")
  

    # # Check if the server call was successful
    # if stats:  # If stats were returned
    #   total_images = stats.get('total_images', 0)
    #   potholes_detected = stats.get('potholes_detected', 0)
    #   potholes_not_detected = stats.get('potholes_not_detected', 0)

    #   print(f"total images processed: {total_images}")
    #   print(f"total potholes detected: {potholes_detected}")
    #   print(f"total not potholes detected: {potholes_not_detected}")
      
    #   # Update the pie chart with the retrieved data
    #   self.plot_pie.data = [
    #     go.Pie(
    #       labels=["Potholes Detected", "Potholes Not Detected"],
    #       values=[potholes_detected, potholes_not_detected]
    #     )
    #   ]
    # else:
    #   alert("Failed to load statistics.")
    
     