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
    selected_image_ids = []

    # Loop through each item in the repeating panel
    for item in self.Review.ItemTemplate5.items:
        checkbox = item['check_box_pothole_exist']  # Adjust based on how your repeating panel is structured
        label = item['label_id']        # Assuming you have a label for the image ID
        
        if checkbox.checked:
            image_id_value = label.text  # Get the image ID from the label text
            selected_image_ids.append(image_id_value)

    if selected_image_ids:
        response = anvil.server.call('save_review', selected_image_ids)
        if response['status'] == 'success':
            print("Reviews updated successfully.")
        else:
            print("Error:", response['message'])
    else:
        print("No images selected.")