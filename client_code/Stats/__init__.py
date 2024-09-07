from ._anvil_designer import StatsTemplate
from anvil import *
import anvil.server
from ._anvil_designer import ReportsTemplate
import plotly.graph_objects as plt


class Stats(StatsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.label_status.text = "No potholes detected."