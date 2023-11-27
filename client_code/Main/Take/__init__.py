from ._anvil_designer import TakeTemplate
from anvil import *
import anvil.server

class Take(TakeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    print(f" I am the Take's INIT")
