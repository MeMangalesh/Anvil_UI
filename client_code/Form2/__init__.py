from ._anvil_designer import Form2Template
from anvil import *
import plotly.graph_objects as go
import anvil.server

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.load_graph()
    # Any code you write here will run before the form opens.

  def load_graph(self):
      # Test plot with manual data
      fig = go.Figure(data=go.Scatter(x=[1, 2, 3], y=[10, 20, 30], mode='lines+markers'))
      
      # Ensure the Plotly chart component is being updated
      #print(self.plot_trend)  # Should not be None or throw an error
     
      # Use the correct attribute to set the figure
      self.plot_trend.figure = fig  # Set the entire figure, not just data
