from ._anvil_designer import IntestineTemplate
from anvil import *
import anvil.server

class Intestine(IntestineTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    # Any code you write here will run before the form opens.







# self.b_room_b.role = "elevated-button"