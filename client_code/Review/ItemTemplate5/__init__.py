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
    #   response = anvil.server.call('save_review', image_id_value)  # Call the server function with the ID
    #   if response['status'] == 'success':
    #       print("Reviewed image updated successfully.")
    #       # Refresh the parent form (Review) to omit the reviewed image
    #       parent_form = get_open_form()  # Get the parent form (Review)
    #       if hasattr(parent_form, 'load_undetected_images'):
    #           parent_form.load_undetected_images()  # Call the load_undetected_images method
    #   else:
    #       print("Error:", response['message'])
    # else:
    #     print("No images selected.")
      try:
          # Call the server function with the ID
          response = anvil.server.call('save_review', image_id_value)  
          
          if response['status'] == 'success':
              print("Reviewed image updated successfully.")
              # Show a success message to the user
              alert("Review saved successfully.", title="Success", large=True)
              
              # Refresh the parent form (Review) to omit the reviewed image
              parent_form = get_open_form()  # Get the parent form (Review)
              if hasattr(parent_form, 'load_undetected_images'):
                  parent_form.load_undetected_images()  # Call the load_undetected_images method
              
          else:
              # Handle error response from the server
              print("Error:", response['message'])
              alert(response['message'], title="Error", large=True)
      
      except Exception as e:
          # Handle any exceptions that may occur
          alert(f"An error occurred: {str(e)}", title="Error", large=True)
  
    else:
          # If the checkbox is not checked, show a warning message
          alert("Please select if a pothole exists before saving.", title="No Selection", large=True)