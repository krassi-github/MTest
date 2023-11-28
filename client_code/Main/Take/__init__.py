from ._anvil_designer import TakeTemplate
from anvil import *
import anvil.server
from ... import Globals

class Take(TakeTemplate):
  def __init__(self, time, med_code):
    # Set Form properties and Data Bindings.
    self.init_components()    # **properties
    #print(properties.items())    

    self.time_box.text = anvil.server.call("get_time")[11:]
    self.medicine.text = Globals.get_med_name(med_code)
    self.pcs_box.text = Globals.get_med_pcs(med_code, time)    


  def ok_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def cancel_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
