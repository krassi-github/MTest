from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server

class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    print(f"ItemTemplate __init__()")
    for i, v in enumerate(Globals.daily_intakes):
      self.dr_time.text = v["rd_time"]
