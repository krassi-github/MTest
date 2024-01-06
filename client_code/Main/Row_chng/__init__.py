from ._anvil_designer import Row_chngTemplate
import time
from anvil import *
import anvil.server
import anvil.js
from anvil.js import window
from ... import Globals
from ... import validation

# daily_intakes FORMAT
# int_id, rd_time, rd_name, rd_weight, rd_pcs

class Row_chng(Row_chngTemplate):
  def __init__(self, int_id):
    # Set Form properties and Data Bindings.
    self.init_components()    # **properties
    self.row = Globals.find_row_in_day("int_id", int_id)
    #self.save_b.width = self.clear_b.width = "95%"
    self.delete_b.background = "red"
    self.delete_b.foreground = "white"
    self.time_box.text = self.row["rd_time"]
    self.time_copy = self.time_box.text
    self.medicine.text = self.row["rd_name"]
    self.pcs_box.text = self.row["rd_pcs"]
    self.pcs_copy = self.pcs_box.text
    self.notes_box.text = self.row["rd_note"]
    Globals.edited_time = None
    Globals.edited_pcs = None
    Globals.edited_notes = None
    #  tp validate form's components
    self.validator = validation.Validator()


  def time_box_lost_focus(self, **event_args):
    self.time_box_pressed_enter()

  def time_box_focus(self, **event_args):
    self.time_copy = self.time_box.text

  def time_box_pressed_enter(self, **event_args):
    if self.time_copy != self.time_box.text:        
      m = ""
      r, m = self.validator.validate_time(self.time_box.text)
      if not r:
        # window.confirm(m)    # test JS call
        self.err_msg("time", m)
      else:
        Globals.edited_time = self.time_box.text

  def pcs_box_lost_focus(self, **event_args):
    self.pcs_box_pressed_enter()

  def pcs_box_focus(self, **event_args):
    self.pcs_copy = self.pcs_box.text

  def pcs_box_pressed_enter(self, **event_args):
    if self.pcs_copy != self.pcs_box.text:
      r, m = self.validator.validate_pcs(self.pcs_box.text)
      if not r:
        # window.confirm(m)
        self.err_msg("pcs", m)
      else:
        Globals.edited_pcs = self.pcs_box.text

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

  def notes_box_lost_focus(self, **event_args):
    if self.notes_box.text:
      Globals.edited_notes = self.notes_box.text

  def save_b_click(self, **event_args):
    r = alert(content="Потвърдете промяна на данни! \nПроцесът е НЕОБРАТИМ!",
            title="Потвърждение",
          buttons=[("ЗАПИС", True), ("Отказ", False)],)
    if r:
      r = Globals.update_intake(self.row["int_id"])
      if not r:
        alert(f"Успешен запис ", title="Съобщение")
        return()
      if r == -1:
        self.msg_box.text = "Няма променени полета"
        self.msg_box.foreground = "red"      
      elif r < 0:
        self.msg_box.text = f"Код  {r}"
        self.msg_box.foreground = "red"
        alert(f"Неуспешен запис  {r}", title="Съобщение")
      time.sleep(3.5)
      self.msg_box.text = ''
      self.msg_box.foreground = "black"

  def clear_b_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def new_b_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def delete_b_click(self, **event_args):
    r = alert(content="Потвърдете ИЗТРИВАНЕ на данни! \nПроцесът е НЕОБРАТИМ!",
            title="Потвърждение",
          buttons=[("ИЗТРИВАНЕ", True), ("Отказ", False)],)
    if r:
      r = Globals.delete_intake(self.row["int_id"])
      if not r:
        alert(f"Успешno изтриване ", title="Съобщение")
      else:
        alert(f"Неуспешно изтриване  {r}", title="Съобщение")

