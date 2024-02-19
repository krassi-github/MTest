from ._anvil_designer import RowTemplate2Template
from anvil import *
import anvil.server
from ... import Globals

# # loaded group of medicine FORMAT [[name, pcs, code], ...... ]

class RowTemplate2(RowTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.medicine_lbl.text = self.item[0]
    self.pcs_box.text = self.item[1]

  def erase_btn_click(self, **event_args):
    r = alert(f"Сигурни ли сте за ИЗТРИВАНЕ на {self.item[0]} ?", buttons=[("Да", True), ("НЕ", False)])
    if r:
      r = alert(f"Потвърдете ИЗТРИВАНЕ на {self.item[0]} !\n Процесът е необратим !", buttons=[("Да", True), ("НЕ", False)])
      if r:
        Globals.erase_group_row(self.item[0])
        self.parent.parent.parent.show_group()

  def pcs_box_focus(self, **event_args):
    """This method is called when the TextBox gets focus"""
    pass

  def pcs_box_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    pass

  def pcs_box_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass
      


    


