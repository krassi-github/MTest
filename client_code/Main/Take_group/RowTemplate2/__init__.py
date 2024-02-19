from ._anvil_designer import RowTemplate2Template
from anvil import *
import anvil.server
from ... import Globals

# loaded group of medicine FORMAT: [[name, pcs, code], ...... ]

class RowTemplate2(RowTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.medicine_lbl.text = self.item[0]
    self.pcs_box.text = self.item[1]
    self.pcs_copy = self.item[1]

  def erase_btn_click(self, **event_args):
    r = alert(f"Сигурни ли сте за ИЗТРИВАНЕ на {self.item[0]} ?", buttons=[("Да", True), ("НЕ", False)])
    if r:
      r = alert(f"Потвърдете ИЗТРИВАНЕ на {self.item[0]} !\n Процесът е необратим !", buttons=[("Да", True), ("НЕ", False)])
      if r:
        Globals.erase_group_row(self.item[0])
        self.parent.parent.parent.show_group()

  def pcs_box_focus(self, **event_args):
    self.pcs_copy = self.pcs_box.text

  def pcs_box_lost_focus(self, **event_args):
    pcs_box_pressed_enter()

  def pcs_box_pressed_enter(self, **event_args):
    if self.pcs_copy != self.pcs_box.text:
      r, m = self.validator.validate_pcs(self.pcs_box.text)
      if not r:
        self.parent.parent.err_msg("pcs", m)
      else:
        Globals.change_pcs(self.item[0], self.pcs_box.text)

      


    


