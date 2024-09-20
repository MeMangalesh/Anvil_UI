from ._anvil_designer import ItemTemplate5Template
from anvil import *
import anvil.server

class ItemTemplate5(ItemTemplate5Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Set the image source, filename, and id using the item passed to the template
    self.image_display.source = "data:image/png;base64," + self.item['image_base64']
    self.label_id.text = str(self.item['id'])  # Assuming you have another Label component for the ID

  def button_save_click(self, **event_args):
    checkbox = self.check_box_pothole_exist
    label = self.label_id       
    
    if checkbox.checked:
      image_id_value = label.text  # Get the image ID from the label text
      response = anvil.server.call('save_review', image_id_value)  # Call the server function with the ID
      if response['status'] == 'success':
          print("Review updated successfully.")
      else:
          print("Error:", response['message'])
    else:
        print("No images selected.")