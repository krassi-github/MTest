from ._anvil_designer import ChangeTemplate
from anvil import *
import anvil.server
from ... import Globals
from ... import validation

class Change(ChangeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens
    # #self.column_panel_1.width = "60%"
    # self.repeating_panel_1.width = "60%"
    self.set_event_handler("x-Date-Change", self.date_change)
    self.label_1.text = Globals.cur_date[:10]
    print(f"Change __init__()")
    Globals.load_intakes(Globals.cur_date)
    self.rp_refresh()


  def date_change(self, **kw):
    self.label_1.text = Globals.cur_date[:10]
    Globals.load_intakes(Globals.cur_date)
    self.rp_refresh()


  def rp_refresh(self):
    self.repeating_panel_1.items = Globals.daily_intakes
  

