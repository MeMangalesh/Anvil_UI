from ._anvil_designer import StatsTemplate
from datetime import datetime
from anvil import *
import plotly.graph_objects as go
import anvil.server
#import plotly.express as px

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
    self.load_heatmap()
    self.load_bar_chart()
    self.load_pothole_feedback_chart()
    

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
    # #test plot with manual data 
    # print(self.plot_trend)
    # fig = go.Figure(data=go.Scatter(x=[1, 2, 3], y=[10, 20, 30], mode='lines+markers'))
    # self.plot_trend.figure = fig #replaced .data with .figure to show the line on the graph
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
            # fig.update_layout(
            #     title="Interactive Potholes Detected Over Time",
            #     xaxis_title="Date",
            #     yaxis_title="Total Potholes Detected",
            #     hovermode="x",
            #     template="plotly_dark"
            # )
          # Update layout to show only the date on the x-axis
            fig.update_layout(
              title="Interactive Potholes Detected Over Time",
              xaxis_title="Date",
              yaxis_title="Total Potholes Detected",
              xaxis=dict(
                tickformat="%b %d, %Y",  # Format the x-axis to show date only
                tickmode='array',
                tickvals=dates
              )
            )
            # Set the figure in a Plotly chart component
            self.plot_trend.figure = fig
        else:
            alert(f"Error: {result['message']}")

    except Exception as e:
        alert(f"Failed to load graph: {str(e)}")

###############
## Heatmap: severity based on confidence score
################
  def load_heatmap(self):
    # Fetch heatmap data from the server
    heatmap_data = anvil.server.call('fetch_severity_heatmap')

    severity_labels = [item['Severity'] for item in heatmap_data]
    counts = [item['Counts'] for item in heatmap_data]

    # Create the heatmap figure using Plotly Graph Objects
    fig = go.Figure(data=go.Heatmap(
        z=[counts],  # Data for heatmap
        x=severity_labels,  # X-axis labels
        y=['Count'],  # Y-axis label
        colorscale='Viridis'
    ))

    # Update layout
    fig.update_layout(
        title='Pothole Severity Heatmap',
        xaxis_title='Severity',
        yaxis_title='Count'
    )

    # Render the figure in Anvil
    self.plot_heatmap.data = fig.data
    self.plot_heatmap.layout = fig.layout


  ################
  ## BAR CHART: potholes by severity level
  ################
  def load_bar_chart(self):
        # Fetch severity data from the server
        severity_data = anvil.server.call('fetch_severity_data')

        # Extract severity labels and their counts
        severity_labels = [item['Severity'] for item in severity_data]
        counts = [item['Counts'] for item in severity_data]

        # Create a bar chart using Plotly Graph Objects
        fig = go.Figure(data=[
            go.Bar(
                x=severity_labels,  # X-axis: Severity labels (Low, Medium, High)
                y=counts,  # Y-axis: Counts of potholes per severity
                marker_color='indianred'  # Bar color
            )
        ])

        # Update the layout of the chart
        fig.update_layout(
            title='Pothole Severity Distribution',
            xaxis_title='Severity',
            yaxis_title='Number of Potholes',
            bargap=0.2  # Adds a small gap between the bars
        )

        # Render the figure in Anvil's Plot component
        self.plot_severity_bar.data = fig.data
        self.plot_severity_bar.layout = fig.layout

#############
###
#############
  def load_pothole_feedback_chart(self):
    # Get the date range from the DatePickers in the UI
    date_from = self.date_picker_from.date
    date_to = self.date_picker_to.date

    # Fetch the figure from the server
    fig = anvil.server.call('fetch_pothole_feedback_chart', date_from, date_to)

    # Render the figure in Anvil
    self.plot_podperfeedback.data = fig.data
    self.plot_podperfeedback.layout = fig.layout
  
   


###################
## CONFUSION MATRIX
###################



