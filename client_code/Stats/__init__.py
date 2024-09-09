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

    # Call the server function to get the statistics
    stats = anvil.server.call('get_stats')

   # Check if the server call was successful
    if stats:  # If stats were returned
      total_images = stats.get('total_images', 0)
      potholes_detected = stats.get('potholes_detected', 0)
      potholes_not_detected = stats.get('potholes_not_detected', 0)
      
      # Update the pie chart with the retrieved data
      self.plot_pie.data = [
        go.Pie(
          labels=["Potholes Detected", "Potholes Not Detected"],
          values=[potholes_detected, potholes_not_detected]
        )
      ]
    else:
      alert("Failed to load statistics.")
    
     