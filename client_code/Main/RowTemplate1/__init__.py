from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
from ... import Globals
from .. Take import Take
from .. Take_group import Take_group

# status FORMAT
'''    s = {"p_id": r[p_id], "name": r[name], "code": r[r_m_code], "morning": r[morning],
         "m_ex": False, "noon": r[noon], "n_ex": False, "evening": r[evening],
         "e_ex": False, "on_need": r[on_need], "o_ex": False}
for Groups:
        s = {"p_id": g[gr_code], "name": g[gr_name], "code": g[gr_type], "morning": None,
         "m_ex": False, "noon": None, "n_ex": False, "evening": None,
         "e_ex": False, "on_need": None, "o_ex": False}
'''

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # code of the medicine
    self.link_1.tag = self.item["p_id"]
    self.link_2.tag=self.link_3.tag=self.link_4.tag=self.link_5.tag = self.item["code"]
    
    # Labels data binding
    self.name.text = self.item["name"]
    self.m.text = self.item["morning"]
    if self.item["m_ex"]:
      self.m.foreground = "red"
    self.n.text = self.item["noon"]
    if self.item["n_ex"]:
      self.n.foreground = "red"
    self.e.text = self.item["evening"]
    if self.item["e_ex"]:
      self.e.foreground = "red"
    self.on.text = self.item["on_need"]
    if self.item["o_ex"]:
      self.on.foreground = "red"
    font_size = 20
    self.name.font_size = font_size
    self.m.font_size = font_size
    self.n.font_size = font_size
    self.e.font_size = font_size
    self.on.font_size = font_size


  def link_1_click(self, **event_args):
    if type(self.link_1.tag) is str:
      if self.link_1.tag.startswith("gr"):
        # a group_name is selected => call (gr_name, gr_type)
        r = alert(Take_group(self.link_1.tag, self.link_2.tag), 
          title="Въведи Група!", 
          buttons=[("ЗАПИС", True), ("Отказ", False)],)
        if r:
          r = alert(content="Потвърдете запис на данни! \nПроцесът е НЕОБРАТИМ!",
          title="Потвърждение",
          buttons=[("ЗАПИС", True), ("Отказ", False)],)
      if r:
        r = Globals.put_group()
        if r < 0:
          alert(f"Неуспешен запис  {r}", title="Съобщение")
        else:
          alert(f"Успешен запис ", title="Съобщение")
        

  def link_2_click(self, **event_args):
    self.take('m', self.link_2.tag)

  def link_3_click(self, **event_args):
    self.take('n', self.link_3.tag)

  def link_4_click(self, **event_args):
    self.take('e', self.link_4.tag)

  def link_5_click(self, **event_args):
    self.take('on', self.link_5.tag)

  def take(self, time, med_code):
    r = alert(Take(time, med_code), 
          title="Въведи Лекарство!", 
          buttons=[("ЗАПИС", True), ("Отказ", False)],)
    if r:
      r = alert(content="Потвърдете запис на данни! \nПроцесът е НЕОБРАТИМ!",
           title="Потвърждение",
          buttons=[("ЗАПИС", True), ("Отказ", False)],)
      if r:
        r = Globals.put_intake()
        if r < 0:
          alert(f"Неуспешен запис  {r}", title="Съобщение")
        else:
          alert(f"Успешен запис ", title="Съобщение")
    self.parent.parent.parent.parent.refresh_data(Globals.cur_date)  # to reach the Main
      
      