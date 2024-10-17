from ._anvil_designer import StatsTemplate
from datetime import date, datetime
from anvil import *
import plotly.graph_objects as go
import anvil.server

####
# from anvil import DatePicker, Button

# import anvil.media
# import pymysql
# from ._anvil_designer import ReportsTemplate


class Stats(StatsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
     # Fetch the min and max dates and update the date pickers
    #self.set_default_date_range()
    # Call a function to load and display stats

    ##comment the 6 lines to work on the line graph
    self.set_date_day()
    # self.reset_date_pickers()
    self.load_speedometer()
    self.load_bubble_chart()
    self.load_pie_plot()
    # self.load_graph()
    # self.load_heatmap()
    # self.load_bar_chart()
    ##comment the 6 lines to work on the line graph
    #self.load_pothole_feedback_chart()
    
    self.feedback_pods_by_date()
#########
## Set default date range
#########
  # def set_default_date_range(self):
  #   try:
  #       # Call the Anvil server function to get the min and max dates
  #       date_range = anvil.server.call('get_min_max_dates')
        
  #       if date_range['status'] == 'success':
  #           # Set the min and max dates for the date pickers
  #           self.date_picker_from.date = date_range['min_date']
  #           self.date_picker_to.date = date_range['max_date']
  #           self.date_picker_from.min_date = date_range['min_date']
  #           self.date_picker_to.max_date = date_range['max_date']
  
  #           # Populate the graph with the default date range
  #           self.update_graph(date_range['min_date'], date_range['max_date'])
  #       else:
  #           alert(f"Error fetching date range: {date_range['message']}")
  #   except Exception as e:
  #       alert(f"Unexpected error: {str(e)}")

  def update_graph(self, date_from, date_to):
    try:
      # Call the Anvil server function to fetch chart data
      fig = anvil.server.call('fetch_pothole_feedback_chart', date_from, date_to)
      self.plot_feedback_chart.data = fig
        
    except ValueError as e:
      # Handle the case where no data is available
      if "No feedback data available" in str(e):
          alert(f"No data available for the selected date range: {date_from} to {date_to}")
      else:
          alert(f"Unexpected error: {str(e)}")

    except Exception as e:
      alert(f"Error updating graph: {str(e)}")


  # def date_picker_from_change(self, **event_args):
  #   # Get the selected dates from the date pickers
  #   date_from = self.date_picker_from.date
  #   date_to = self.date_picker_to.date

  #   # Update the graph with the selected date range
  #   self.update_graph(date_from, date_to)
 
  ############
  ## Display today's date & day 
  ############
  def set_date_day(self):
  # Get today's date
      today = date.today()
      # Extract day, month, and year separately
      day_of_week = today.strftime("%A").upper()  # Example: Tuesday
      date_today = today.day  # Example: 26
      month = today.strftime("%B").upper()  # Example: September
      year = today.year  # Example: 2023
      
      # Assign values to the labels
      self.label_day.text = day_of_week  # Label for the day of the week
      self.label_date.text = str(date_today)  # Label for the date of the month
      self.label_month.text = month  # Label for the month
      self.label_year.text = str(year)  # Label for the year
  
  ##############
  ## Update date picker
  ##############
  
  # # Function to call the server for min and max dates
  # def fetch_min_max_dates(self):
  #     try:
  #         # Call the VSCode uplink function to get the min and max dates
  #         response = anvil.server.call('get_min_max_dates')

  #         if response['status'] == 'success':
  #             min_date = response['min_date']
  #             max_date = response['max_date']

  #             # Update the date pickers with the min and max dates
  #             self.update_date_pickers(min_date, max_date)
  #         else:
  #             alert(f"Error: {response['message']}")
      
  #     except Exception as e:
  #         alert(f"Unexpected error: {str(e)}")

  #   # Function to update date pickers
  # def update_date_pickers(self, min_date, max_date):
  #     # Set the min and max dates for the date pickers
  #     self.date_picker_from.min_date = min_date
  #     self.date_picker_to.min_date = min_date
  #     self.date_picker_from.max_date = max_date
  #     self.date_picker_to.max_date = max_date

  #     # Optionally, set today's date as the default
  #     today = date.today()
  #     self.date_picker_from.date = today
  #     self.date_picker_to.date = today

  ###############
  ## Reset Date Picker
  ###############
  # def reset_date_pickers(self):
  #   # Set the date pickers to today
  #   today = date.today()
  #   self.date_picker_from.date = today
  #   self.date_picker_to.date = today

  #   # Deactivate older dates (minimum date)
  #   self.date_picker_from.min_date = today
  #   self.date_picker_to.min_date = today

 ################
  ## Speedometer: Avg Confidence Score 
  ################
  def load_speedometer(self):
    # Fetch the average max confidence score from the server
    avg_max_conf_score = anvil.server.call('fetch_avg_max_conf_score')
    # print(f"avg_max_conf_score: {avg_max_conf_score}")
    
    if avg_max_conf_score['status'] == "success":
      value = round(avg_max_conf_score['avg_max_conf_score'], 2)

      # Create a speedometer (gauge chart) using Plotly
      fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,  # Set the needle value to the avg max confidence score
        # title={'text': "Average Max Confidence Score", 'font': {'size': 24}},
        gauge={
                'axis': {'range': [0, 1], 'tickvals': [0, 0.33, 0.66, 1], 'ticktext': ['Low', 'Medium', 'High', 'Max'], 'ticks': "outside"},
                'bar': {'color': "gray"},  # Needle color
                'steps': [
                     {'range': [0, 0.33], 'color': "red"},    # First segment (0-0.33)
                        {'range': [0.33, 0.67], 'color': "yellow"},  # Second segment (0.33-0.67)
                        {'range': [0.67, 1], 'color': "green"},  # Third segment (0.67-1)
                    ],
                'threshold': {
                    #'line': {'color': "red", 'width': 4},
                     'line': {'color': "black",'width': 4},  # Make the threshold line invisible  - replaced transparent
                    'thickness': 0.75,
                    'value': value  # Set the threshold line at the needle's position
                 }
              }
         ))
      # Set layout
      fig.update_layout(
          title='Average Max Confidence Score Gauge',
          # xaxis_title='Number of Potholes Detected',
          # yaxis_title='Frequency of Incidents',
          hovermode='closest'
      )
      # Display the speedometer in the designated plot component
      self.plot_speedometer.figure = fig

    else:
        self.label_status.text = "Error loading data: " + avg_max_conf_score['message']

  ##############
  ## Bubble Chart 
  ###############

  def load_bubble_chart(self):
    # Fetch pothole bubble data
    data = anvil.server.call('get_pothole_bubble_data')  # Call your server function to get data

    # Create bubble chart
    fig = go.Figure(data=[
        go.Scatter(
            x=data['pothole_counts'],
            y=data['frequencies'],
            mode='markers',
            marker=dict(
                size=[score * 20 for score in data['avg_conf_scores']],  # Bubble size
                color=data['avg_conf_scores'],  # Color based on average confidence scores
                colorscale='Viridis',
                showscale=True
            ),
            text=data['avg_conf_scores'],  # Hover text
        )
    ])

    # Set layout
    fig.update_layout(
        title='Pothole Frequency Bubble Chart',
        xaxis_title='Number of Potholes Detected',
        yaxis_title='Frequency of Incidents',
        hovermode='closest'
    )

    # Render the figure in the Anvil plot component
    self.plot_bubble_chart.figure = fig  # Assuming you have a plot component named `plot_bubble_chart`

  
  ################
  ## Summary data & Pie Chart
  ################
  def load_pie_plot(self):
    try:
        # Call the server function to get the statistics
        # print("About to call the VSCode")
        response = anvil.server.call("get_pie_plot")
        # print("returning from VSCode")

        # Check the response status
        if response['status'] == "success":
            # Unpack the data correctly
            total_images, potholes_detected = response['data']
            
            # print(f"Total images: {total_images}")
            # print(f"Total potholes detected: {potholes_detected}")

            # Display the total number of images processed & number of potholes detected
            self.label_feedback_count.text = str(total_images)  # Ensure to convert to str
            self.label_detected_count.text = str(potholes_detected)  # Ensure to convert to str

            # Optionally, calculate potholes not detected and update your pie chart if needed
            potholes_not_detected = total_images - potholes_detected
            
            # Update the pie chart with the retrieved data
            self.plot_pie.data = [
                go.Pie(
                    labels=["Potholes Detected", "Potholes Not Detected"],
                    values=[potholes_detected, potholes_not_detected],
                )
            ]
        else:
            alert(f"Error loading statistics: {response['message']}")

    except Exception as e:
        # Handle the case where the server call fails or returns unexpected data
        alert(f"Error loading statistics: {str(e)}")

  # def load_pie_plot(self):
  #   try:
  #     # Call the server function to get the statistics
  #     print("About to call the VSCode")
  #     response = anvil.server.call("get_pie_plot")
  #     print("returning from VSCOde")
  #     print("total images:{total_images}")
  #     # total_images = response['total_images']
  #     # potholes_detected = response['potholes_detected']

  #     print(f"total images:{total_images}")
  #     print(f"total potholes_detected:{potholes_detected}")
  #     # Validate the values to ensure they are integers
  #     # if isinstance(total_images, int) and isinstance(potholes_detected, int):
  #     #   # Calculate potholes not detected
  #     #   potholes_not_detected = total_images - potholes_detected

  #     # Print debug information
  #     print(f"total images processed: {total_images}")
  #     print(f"total potholes detected: {potholes_detected}")
  #     # print(f"total not potholes detected: {potholes_not_detected}")

  #     # Display the total number of images processed & Number of potholes detected
  #     self.label_feedback_count.text = total_images
  #     self.label_detected_count.text = potholes_detected

  #     # Update the pie chart with the retrieved data
  #     # self.plot_pie.data = [
  #     #   go.Pie(
  #     #     labels=["Potholes Detected", "Potholes Not Detected"],
  #     #     values=[potholes_detected, potholes_not_detected],
  #     #   )
  #     # ]
  #   except Exception as e:
  #     # Handle the case where the server call fails or returns unexpected data
  #     alert(f"Error loading statistics: {str(e)}")

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
      result = anvil.server.call("fetch_pothole_trends")

      if result["status"] == "success":
        data = result["data"]

        # Extract data for Plotly
        dates = [item["detection_date"] for item in data]
        counts = [item["total_potholes_count"] for item in data]

        # Debug: Print the data
        # print("Dates:", dates)
        # print("Counts:", counts)

        # Create Plotly figure
        fig = go.Figure(data=go.Scatter(x=dates, y=counts, mode="lines+markers"))

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
            tickmode="array",
            tickvals=dates,
          ),
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
    heatmap_data = anvil.server.call("fetch_severity_heatmap")

    severity_labels = [item["Severity"] for item in heatmap_data]
    counts = [item["Counts"] for item in heatmap_data]

    # Create the heatmap figure using Plotly Graph Objects
    fig = go.Figure(
      data=go.Heatmap(
        z=[counts],  # Data for heatmap
        x=severity_labels,  # X-axis labels
        y=["Count"],  # Y-axis label
        colorscale="Viridis",
      )
    )

    # Update layout
    fig.update_layout(
      title="Pothole Severity Heatmap", xaxis_title="Severity", yaxis_title="Count"
    )

    # Render the figure in Anvil
    self.plot_heatmap.data = fig.data
    self.plot_heatmap.layout = fig.layout

  ################
  ## BAR CHART: potholes by severity level
  ################
  def load_bar_chart(self):
    # Fetch severity data from the server
    severity_data = anvil.server.call("fetch_severity_data")

    # Extract severity labels and their counts
    severity_labels = [item["Severity"] for item in severity_data]
    counts = [item["Counts"] for item in severity_data]

    # Create a bar chart using Plotly Graph Objects
    fig = go.Figure(
      data=[
        go.Bar(
          x=severity_labels,  # X-axis: Severity labels (Low, Medium, High)
          y=counts,  # Y-axis: Counts of potholes per severity
          marker_color="indianred",  # Bar color
        )
      ]
    )

    # Update the layout of the chart
    fig.update_layout(
      title="Pothole Severity Distribution",
      xaxis_title="Severity",
      yaxis_title="Number of Potholes",
      bargap=0.2,  # Adds a small gap between the bars
    )

    # Render the figure in Anvil's Plot component
    self.plot_severity_bar.data = fig.data
    self.plot_severity_bar.layout = fig.layout

  #############
  ### Feedback vs Potholes Detected - OK
  #############
  def feedback_pods_by_date(self):
    #Call the Anvil server function to get data
    results = anvil.server.call('fetch_feedback_and_potholes')
    
  # Debug: Print the results to check the structure
    #print(results)  # or use anvil.server.call to log if running in Anvil

    formatted_results = []
    for row in results:
      formatted_results.append({
            "feedback_date": row['feedback_date'],  # Accessing the date directly
            "feedback_count": int(row['feedback_count']),  # Ensure this is an int
            "total_potholes_detected": int(row['total_potholes_detected'])  # Ensure this is an int
        })
    
    # Create the plot
    fig = go.Figure()
    
    # Extract dates, feedback counts, and potholes detected for plotting
    dates = [row['feedback_date'] for row in formatted_results]
    feedback_counts = [row['feedback_count'] for row in formatted_results]
    total_potholes_detected = [row['total_potholes_detected'] for row in formatted_results]

     # Create the plot using the full figure declaration
    fig = go.Figure(
        data=[
            go.Scatter(
                x=dates, 
                y=feedback_counts, 
                mode='lines+markers', 
                name='Feedback Count',
                line=dict(color='blue')
            ),
            go.Scatter(
                x=dates, 
                y=total_potholes_detected, 
                mode='lines+markers', 
                name='Total Potholes Detected',
                line=dict(color='red')
            )
        ]
    )

    # Update layout
    fig.update_layout(
        title='Daily Feedback Count and Potholes Detected',
        xaxis_title='Date',
        yaxis_title='Count',
        legend_title='Legend'
    )

     # Render the figure in Anvil's Plot component
    self.plot_podperfeedback.data = fig.data
    self.plot_podperfeedback.layout = fig.layout
  ###################
  ## CONFUSION MATRIX
  ###################

  def button_click(self, **event_args):
    # Get selected dates from the date pickers
    date_from = self.date_picker_from.date
    date_to = self.date_picker_to.date

    # Call the Anvil server function that fetches the feedback chart data
    result = anvil.server.call("fetch_pothole_feedback_chart", date_from, date_to)

    # Now `result` contains the feedback data, and you can plot it or use it in your chart
    print(result)



