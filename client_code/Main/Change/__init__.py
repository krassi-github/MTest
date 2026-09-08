from ._anvil_designer import ChangeTemplate
from anvil import *
import anvil.server
from ... import Globals
from ... import validation


class Change(ChangeTemplate):
  def __init__(self, main_form=None, **properties):
    self.init_components(**properties)
    # #self.column_panel_1.width = "60%"
    # self.repeating_panel_1.width = "60%"
    self.main_form = main_form
    self.set_event_handler("x-Date-Change", self.date_change)
    self.date_change()


  def date_change(self, **kw):
    self.label_1.text = Globals.cur_date[:10]
    Globals.load_intakes(Globals.cur_date)
    self.rp_refresh()


  def rp_refresh(self):
    self.repeating_panel_1.items = Globals.daily_intakes

  @handle("back_btn", "click")
  def back_btn_click(self, **event_args):
    Globals.mode = "create"
    self.main_form.show_main_content()
  

