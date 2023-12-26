from ._anvil_designer import ChangeTemplate
from anvil import *
import anvil.server
from ... import Globals
from ... import validation

class Change(ChangeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.set_event_handler("x-Date-Change", self.date_change)
    self.label_1.text = Globals.cur_date
    print(f"Change __init__()")
    Globals.load_intakes(Globals.cur_date)
    self.repeating_panel_1.items = Globals.daily_intakes
    for i, v in enumerate(Globals.daily_intakes):
      self.ItemTemplate1.dr_time.text = v["rd_time"]


  def date_change(self, **kw):
    Globals.load_intakes(Globals.cur_date)
    # self.repeating_panel_1.items = Globals.daily_intakes
    print(f"date_change()")
    for i, v in enumerate(Globals.daily_intakes):
      self.dr_time.text = v["rd_time"]
