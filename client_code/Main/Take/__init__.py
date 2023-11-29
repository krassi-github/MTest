from ._anvil_designer import TakeTemplate
from anvil import *
import anvil.server
import anvil.js
from anvil.js import window
from ... import Globals
from ... import validation
from ... Form1 import Form1

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
    Form1.call_js('showJsAlert', 'Грешка')
  

  def time_box_lost_focus(self, **event_args):
    self.time_box_pressed_enter()
    
  def time_box_change(self, **event_args):
    #self.time_box_pressed_enter()
    pass

  def time_box_pressed_enter(self, **event_args):
    r, m = self.validator.validate_time(self.time_box.text)
    print(f"Time validation r= {r}  ")
    if not r:      
      # window.confirm(m)
      self.time_box.scroll_into_view(smooth=True)
      self.text_box.background = 'pink'
      self.text_box.placeholder = 'Class Name Required'
      self.text_box.align = 'center'
      time.sleep(1.5) #Ensures that the warning text persists for ~1.5 seconds 
      self.text_box.background = None
      self.text_box.placeholder = None
      self.text_box.align = 'left'
      return()
    else:
      Globals.intake_time = self.time_box.text

  def pcs_box_lost_focus(self, **event_args):
    self.pcs_box_pressed_enter()

  def pcs_box_change(self, **event_args):
    self.pcs_box_pressed_enter()

  def pcs_box_pressed_enter(self, **event_args):
    pass

