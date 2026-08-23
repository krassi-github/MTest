from ._anvil_designer import IntestineTemplate
from anvil import *
import anvil.server

from .. import validation
from . Intestine_more import Intestine_more

import datetime

class Intestine(IntestineTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    self.date_picker_1.format = "%Y/%m/%d %H:%M"
    if self.date_picker_1.date is None:
      #self.date_picker_1.date = datetime.datetime.now()
      self.date_picker_1.pick_time = True
      self.date_picker_1.date = datetime.datetime.now()
      self.date_picker_1.min_date = "2026/08/21 00:00"
      self.date_picker_1.max_date = (self.date_picker_1.date + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
      self.datetime_box.text = "ДНЕС Е " + self.date_picker_1.date.strftime("%Y-%m-%d %H:%M")[:10] + '     '

    self.bristol = None
    self.relief = None
    self.strain = None

    self.L = None
    self.N = None
    self.mucus = None
    self.blood = None
    self.note = None
    
    # Link handlers to buttons
    for i in range(1, 8):
      b = getattr(self, f"bristol_{i}")
      b.tag = i
      b.set_event_handler("click", self.bristol_click)
    for i in range(1, 4):
      b = getattr(self, f"relief_{i}")
      b.tag = i
      b.set_event_handler("click", self.relief_click)    
    for i in range(4):
      b = getattr(self, f"strain_{i}")
      b.tag = i
      b.set_event_handler("click", self.strain_click)

    self.validator = validation.Validator()


  # Handlers
  def bristol_click(self, sender, **event_args):
    self.bristol = sender.tag
    for i in range(1, 8):
      b = getattr(self, f"bristol_{i}")
      b.role = "filled-button" if b.tag == self.bristol else ""      
        
  def relief_click(self, sender, **event_args):
    self.relief = sender.tag
    for i in range(1, 4):
      b = getattr(self, f"relief_{i}")
      b.role = "filled-button" if b.tag == self.relief else ""
      #print("This b= ", b)

  def strain_click(self, sender, **event_args):
    self.strain = sender.tag
    for i in range(4):
      b = getattr(self, f"strain_{i}")
      b.role = "filled-button" if b.tag == self.strain else ""

  @handle("more", "click")
  def more_click(self, **event_args):
    frm = Intestine_more(
    L=self.L,
    N=self.N,
    mucus=self.mucus,
    blood=self.blood,
    note=self.note
    )

    ok = alert(
      content=frm,
      title="Допълнително",
      buttons=[
        ("ОТКАЗ", False),
        ("OK", True)
      ]
    )
  
    if ok:
      self.L = int(frm.tb_L.text) if frm.tb_L.text else None
      self.N = int(frm.tb_N.text) if frm.tb_N.text else None
      self.mucus = frm.cb_mucus.checked
      self.blood = frm.cb_blood.checked
      self.note = frm.ta_note.text
      print(f"{self.L}  {self.N}  // {self.mucus}    {self.blood}  {self.note}")


      