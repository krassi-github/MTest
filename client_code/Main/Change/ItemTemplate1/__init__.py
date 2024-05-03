from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server
from .... import Globals
from ... Row_chng import Row_chng


class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    #for key, value in properties.items():
      #print(f"** key {key}: #  value {value}")
    self.init_components(**properties)
    self.dr_time.text = self.item["rd_time"]
    self.dr_med.text = self.item["rd_name"]
    self.dr_qty.text = self.item['rd_weight']
    self.dr_pcs.text = self.item['rd_pcs']
    self.dr_time.tag = self.item["int_id"]      # Globals.intakes

  def link_1_click(self, **event_args):
    Globals.sorting()
    self.parent.parent.rp_refresh()

  def dr_time_focus(self, **event_args):
    self.chng_start()

  def dr_pcs_focus(self, **event_args):
    self.chng_start()

  def chng_start(self):
    self.parent.parent.label_1.text += f"   {self.item['int_id']}"
    r = alert(Row_chng(self.dr_time.tag), 
          title="Редактирай прием!", 
          buttons=[("ИЗХОД", True), ("Отказ", False)],)
    self.__init__()
    self.link_1_click()
    
