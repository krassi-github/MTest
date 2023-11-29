from ._anvil_designer import TakeTemplate
from anvil import *
import anvil.server
from ... import Globals
from ... import validation

class Take(TakeTemplate):
  def __init__(self, time, med_code):
    # Set Form properties and Data Bindings.
    self.init_components()    # **properties
    self.time_box.text = anvil.server.call("get_time")[11:]
    Globals.intake_time = self.time_box.text
    self.medicine.text = Globals.get_med_name(med_code)
    self.pcs_box.text, self.type.text = Globals.get_pcs_type(med_code, time)
    Globals.intake_pcs = self.pcs_box.text
    #  validate a form
    self.validator = validation.Validator()
  

  def time_box_lost_focus(self, **event_args):
    time_box_pressed_enter()
    
  def time_box_change(self, **event_args):
    time_box_pressed_enter()

  def time_box_pressed_enter(self, **event_args):
    
    Globals.intake_time = self.time_box.text

  def pcs_box_lost_focus(self, **event_args):
    pcs_box_pressed_enter()

  def pcs_box_change(self, **event_args):
    pcs_box_pressed_enter()

  def pcs_box_pressed_enter(self, **event_args):
    r, m = self.validator.validate_time(self.time_box_text)
    