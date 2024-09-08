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
    if stats['status'] == 'success':
      total_images = stats['data']['total_images']
      potholes_detected = stats['data']['potholes_detected']
      potholes_not_detected = stats['data']['potholes_not_detected']
      
      # Update the pie chart with the retrieved data
      self.plot_1.data = [
        go.Pie(
          labels=["Potholes Detected", "Potholes Not Detected"],
          values=[potholes_detected, potholes_not_detected]
        )
      ]
    else:
      alert("Failed to load statistics: " + stats['message'])

     