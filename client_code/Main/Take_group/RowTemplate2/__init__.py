from ._anvil_designer import RowTemplate2Template
from anvil import *
import anvil.server

class RowTemplate2(RowTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.medicine_lbl.text = "will come"
    self.pcb_box.text = "is coming"
    


