from ._anvil_designer import StatsTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
#import anvil.media
#import pymysql
#from ._anvil_designer import ReportsTemplate

class Stats(StatsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Call a function to load and display stats
    self.load_stats()
    self.load_graph()

  ################
  ## Pie Chart: Total vs Detected 
  ################
  def load_stats(self):
    try:
      # Call the server function to get the statistics
      print("About to call the VSCode")
      response = anvil.server.call('get_stats')
      print("returning from VSCOde")

      total_images = response['total_images']
      potholes_detected = response['potholes_detected']      # Validate the values to ensure they are integers
      if isinstance(total_images, int) and isinstance(potholes_detected, int):
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

  ################
  ## Line Chart: Potholes Count vs. Time 
  ################
  def load_graph(self):
          # Fetch pothole trends from the server
          try:
              result = anvil.server.call('fetch_pothole_trends')
              
              if result['status'] == 'success':
                  data = result['data']
                  
                  # Extract data for Plotly
                  dates = [item['detection_date'] for item in data]
                  counts = [item['total_potholes_count'] for item in data]

                  # Debug: Print the data
                  print("Dates:", dates)
                  print("Counts:", counts)
                
                  # Create Plotly figure
                  fig = go.Figure(data=go.Scatter(x=dates, y=counts, mode='lines+markers'))
                  
                  # Customize the layout
                  fig.update_layout(
                      title="Interactive Potholes Detected Over Time",
                      xaxis_title="Date",
                      yaxis_title="Total Potholes Detected",
                      hovermode="x",
                      template="plotly_dark"
                  )
                  # Set the figure in a Plotly chart component
                  self.plot_trend.data = fig
                  
              else:
                  alert(f"Error: {result['message']}")
  
          except Exception as e:
              alert(f"Failed to load graph: {str(e)}")