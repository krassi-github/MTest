from ._anvil_designer import IntestineTemplate
from anvil import *
import anvil.server

from .. import validation
from . Intestine_more import Intestine_more

import datetime

class Intestine(IntestineTemplate):
  def __init__(self, main_form=None, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    self.main_form = main_form
    self.date_picker_1.format = "%Y/%m/%d %H:%M"
    if self.date_picker_1.date is None:
      #self.date_picker_1.date = datetime.datetime.now()
      self.date_picker_1.pick_time = True
      self.date_picker_1.date = datetime.datetime.now()
      self.date_picker_1.min_date = "2026/08/21 00:00"
      self.date_picker_1.max_date = (self.date_picker_1.date + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M")
      self.datetime_box.text = "ДНЕС Е " + self.date_picker_1.date.strftime("%Y-%m-%d %H:%M")[:10] + '     '

    self.clear_vars()   
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


  def clear_vars(self):
    self.bristol = None
    self.relief = None
    self.strain = None

    self.L = None
    self.N = None
    self.mucus = None
    self.blood = None
    self.note = None

    self.last_row = None


  def clear_fields(self):
    for i in range(1, 8):
      getattr(self, f"bristol_{i}", None).role = ''
    for i in range(1, 4):
      b = getattr(self, f"relief_{i}", None).role = ''   
    for i in range(4):
      b = getattr(self, f"strain_{i}", None).role = ''

      
  # Handlers
  def bristol_click(self, sender, **event_args):
    self.bristol = sender.tag
    for i in range(1, 8):
      b = getattr(self, f"bristol_{i}")
      b.role = "filled-button" if b.tag == self.bristol else ""
    self.save_btn.background = None if self.bristol is None or self.relief is None or\
    self.strain is None else "#DFF2DF"
        
  def relief_click(self, sender, **event_args):
    self.relief = sender.tag
    for i in range(1, 4):
      b = getattr(self, f"relief_{i}")
      b.role = "filled-button" if b.tag == self.relief else ""
      self.save_btn.background = None if self.bristol is None or self.relief is None or\
      self.strain is None else "#DFF2DF"

  def strain_click(self, sender, **event_args):
    self.strain = sender.tag
    for i in range(4):
      b = getattr(self, f"strain_{i}")
      b.role = "filled-button" if b.tag == self.strain else ""
      self.save_btn.background = None if self.bristol is None or self.relief is None or\
      self.strain is None else "#DFF2DF"

  @handle("more_btn", "click")
  def more_btn_click(self, **event_args):
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
      #print(f"{self.L}  {self.N}  // {self.mucus}    {self.blood}  {self.note}")

  @handle("save_btn", "click")
  def save_btn_click(self, **event_args):
    if None in (self.bristol, self.relief, self.strain):
      alert("ИЗБЕРЕТЕ СТОЙНОСТ ЗА ВСЕКИ РЕД!\n \nВ раздел ОЩЕ\nПолетата не са задължителни", title="ВНИМАНИЕ!")
      return
    r = alert(f"Бристол {self.bristol}\nОблекчение {self.relief}\nНапън {self.strain}\n"
          f"L= {self.L}\n"
          f"N= {self.N}",
          title="ПОТВЪРДИ ЗАПИС", buttons=[("ЗАПИС", True), ("Отказ", False)], )
    if r:
      row = anvil.server.call("save_intestine_event", None, self.date_picker_1.date.strftime("%Y-%m-%d %H:%M").replace("-", "/"), 
      self.bristol, self.relief, self.strain, 
      self.L, self.N,
      self.mucus, self.blood,
      self.note)
      if not row:
        alert("====== NO ======\nНЕУСПЕШЕН ЗАПИС", title = "Съобщение")
      else:
        alert("УСПЕШЕН ЗАПИС", title = "Съобщение")
        self.last_row = row
        self.clear_vars()
        self.clear_fields()
        self.save_btn.background = None
        

  @handle("cancel_btn", "click")
  def cancel_btn_click(self, **event_args):
    self.main_form.show_main_content()
