from ._anvil_designer import ImagePopupTemplate
from anvil import *
import anvil.server

class ImagePopup(ImagePopupTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        self.close_button.set_event_handler("click", self.close)  # Bind the close method
        self.visible = False  # Start with the modal hidden

    def show(self):
        self.visible = True  # Show the modal
        self.image.visible = True  # Show the image component

    def hide(self):
        self.visible = False  # Hide the modal
        self.image.visible = False  # Hide the image component

    def close(self, **event_args):
        self.hide()  # Hide the modal when the close button is clicked
