from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
from ... import Globals
from .. Take import Take

# status FORMAT
'''    s = {"p_id": r[p_id], "name": r[name], "code": r[r_m_code], "morning": r[morning],
         "m_ex": False, "noon": r[noon], "n_ex": False, "evening": r[evening],
         "e_ex": False, "on_need": r[on_need], "on_ex": False}'''

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # code of the medicine
    self.link_2.tag=self.link_3.tag=self.link_4.tag=self.link_5.tag = self.item["code"]    
    # Labels data bunding
    self.name.text = self.item["name"]
    self.m.text = self.item["morning"]
    self.n.text = self.item["noon"]
    self.e.text = self.item["evening"]
    self.on.text = self.item["on_need"]

    font_size = 20
    self.name.font_size = font_size
    self.m.font_size = font_size
    self.n.font_size = font_size
    self.e.font_size = font_size
    self.on.font_size = font_size

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

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
      
    
  


