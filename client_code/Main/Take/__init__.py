from ._anvil_designer import TakeTemplate
import time
from anvil import *
import anvil.server
import anvil.js
from anvil.js import window
from ... import Globals
from ... import validation

class Take(TakeTemplate):
  def __init__(self, time, med_code):
    # Set Form properties and Data Bindings.
    self.init_components()    # **properties
    self.time_box.text = anvil.server.call("get_time")[11:]
    Globals.intake_time = self.time_box.text
    self.time_copy = self.time_box.text
    self.medicine.text = Globals.get_med_name(med_code)
    self.pcs_box.text, self.type.text = Globals.get_pcs_type(med_code, time)
    Globals.intake_pcs = self.pcs_box.text
    self.pcs_copy = self.pcs_box.text
    #  tp validate a form components
    self.validator = validation.Validator()
  

  def time_box_lost_focus(self, **event_args):
    self.time_box_pressed_enter()
    
  def time_box_focus(self, **event_args):
    self.time_copy = self.time_box.text

  def time_box_pressed_enter(self, **event_args):
    r, m = self.validator.validate_time(self.time_box.text)
    if not r:      
      # window.confirm(m)
      self.err_msg(self.time_box, m)
    else:
      Globals.intake_time = self.time_box.text

  def pcs_box_lost_focus(self, **event_args):
    self.pcs_box_pressed_enter()

  def pcs_box_focus(self, **event_args):
    self.pcs_copy = self.pcs_box.text


  def pcs_box_pressed_enter(self, **event_args):
    pass





