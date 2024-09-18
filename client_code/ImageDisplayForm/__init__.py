from ._anvil_designer import ImageDisplayFormTemplate
from anvil import *
import anvil.server


class ImageDisplayForm(ImageDisplayFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
       
    # Set the image source to the base64 string
    self.image_display.source = f"data:image/png;base64,{image_base64}"
