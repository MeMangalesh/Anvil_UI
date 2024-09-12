from ._anvil_designer import FormtestTemplate
from anvil import *
import anvil.server


class Formtest(FormtestTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    
