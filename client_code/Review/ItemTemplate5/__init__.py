from ._anvil_designer import ItemTemplate5Template
from anvil import *
from datetime import datetime, date
# from . import ImagePopup  # Import the new ImagePopup form
import anvil.server


class ItemTemplate5(ItemTemplate5Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Set the image source, filename, and id using the item passed to the template
    self.image_display.source = "data:image/png;base64," + self.item['image_base64']
    self.label_id.text = str(self.item['id'])  # Assuming you have another Label component for the ID
    # self.label_processed_dt.text = str(self.item['processed_dt'])
    
    # # Handle `processed_dt` - format as a string if present, otherwise set to "N/A"
    # if 'processed_dt' in self.item and self.item['processed_dt']:
    #   # # Format the date if it's a datetime object, otherwise convert to string
    #   # if isinstance(self.item['processed_dt'], datetime):
    #   #     formatted_date = self.item['processed_dt'].strftime("%Y-%m-%d")
    #   # else:
    #   #     formatted_date = str(self.item['processed_dt'])  # In case it's already a string
    #   # print(f"Processed date: {formatted_date}")
    #   self.label_processed_dt.text = self.item['processed_dt']
    # else:
    #     self.label_processed_dt.text = "N/A"  # Handle missing date if necessary

    # Assign the CSS class 'enlarge-on-hover' to the image for hover effect
    # self.image_display.role = 'enlarge-on-hover'
    # print(f"Role set for image: {self.image_display.role}")
#######################################
  # code above replaced with below
#######################################
  # def __init__(self, **properties):
  #   # Set Form properties and Data Bindings.
  #   self.init_components(**properties)

  #   # Set the image source, filename, and id using the item passed to the template
  #   self.image_display.source = "data:image/png;base64," + self.item['image_base64']
  #   self.label_id.text = str(self.item['id'])  # Assuming you have another Label component for the ID

  #   # Assign the CSS class 'enlarge-on-hover' to the image
  #   self.image_display.role = 'enlarge-on-hover'

  #   # Bind the hover event
  #   self.image_display.bind("mouseenter", self.show_popup)
  #   self.image_display.bind("mouseleave", self.hide_popup)

  #   self.popup = ImagePopup()  # Create an instance of the popup

  #   def show_popup(self, **event_args):
  #       # Set the image source in the popup
  #       self.popup.image.source = self.image_display.source
  #       self.popup.show()  # Display the popup

  #   def hide_popup(self, **event_args):
  #       self.popup.hide()  # Hide the popup
  #################################
  
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