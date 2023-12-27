from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server
from .... import Globals

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

  def link_1_click(self, **event_args):
    Globals.sorting()
    self.parent.parent.rp_refresh()
    