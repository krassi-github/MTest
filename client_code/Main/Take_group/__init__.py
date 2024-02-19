from ._anvil_designer import Take_groupTemplate
import time
from anvil import *
import anvil.server
#import anvil.js
#from anvil.js import window
from ... import Globals
from ... import validation

class Take_group(Take_groupTemplate):
  def __init__(self, gr_name, gr_type):
    # Set Form properties and Data Bindings.
    self.init_components()    # **properties

    self.time_box.text = anvil.server.call("get_time")[11:]
    Globals.intake_time = self.time_box.text
    self.time_copy = self.time_box.text
    r = Globals.load_group(gr_name, gr_type)
    if r < 0:
      self.err_msg("msg", f" Code= {r}")
    else:
      self.show_group()

    #  tp validate form's components
    self.validator = validation.Validator()

  
  def show_group(self):
    self.repeating_panel_1.items = Globals.med_group

  
  def time_box_lost_focus(self, **event_args):
    self.time_box_pressed_enter()

  def time_box_focus(self, **event_args):
    self.time_copy = self.time_box.text

  def time_box_pressed_enter(self, **event_args):
    m = ""
    r, m = self.validator.validate_time(self.time_box.text)
    if not r:
      self.err_msg("time", m)
    else:
      Globals.intake_time = self.time_box.text

  def pcs_box_lost_focus(self, **event_args):
    self.pcs_box_pressed_enter()

  def pcs_box_focus(self, **event_args):
    self.pcs_copy = self.pcs_box.text

  def pcs_box_pressed_enter(self, **event_args):
    r, m = self.validator.validate_pcs(self.pcs_box.text)
    if not r:
      # window.confirm(m)
      self.err_msg("pcs", m)
    else:
      Globals.intake_pcs = self.pcs_box.text

  def err_msg(self, box: str, msg):
    self.time_box.scroll_into_view(smooth=True)
    if box == "time":
      self.time_box.background = 'pink'
    elif box == "pcs":
      self.pcs_box.background = 'pink'
    self.msg_box.text = msg
    self.msg_box.foreground = "red"
    time.sleep(3.5) #Ensures that the warning text persists for ~1.5 seconds
    if box == "time":
      self.time_box.background = None
      self.time_box.text = self.time_copy
    elif box == "pcs":
      self.pcs_box.background = None
      self.pcs_box.text = self.pcs_copy
    self.msg_box.text = ""

  def notes_lost_focus(self, **event_args):
    Globals.intake_notes = self.notes.text
