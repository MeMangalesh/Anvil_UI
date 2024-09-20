from ._anvil_designer import ItemTemplate5Template
from anvil import *
import anvil.server

class ItemTemplate5(ItemTemplate5Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
# Set the image source, filename, and id using the item passed to the template
    self.image_display.source = "data:image/png;base64," + self.item['image_base64']
    self.label_id.text = str(self.item['id'])  # Assuming you have another Label component for the ID

  def button_save_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
