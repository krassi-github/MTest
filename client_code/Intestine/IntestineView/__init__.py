from ._anvil_designer import IntestineViewTemplate
from anvil import *
import anvil.server
from ... import Globals

import datetime

'''
class IntestineView(IntestineViewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    mode = Globals.intestine_view_mode if Globals.intestine_view_mode else 'D'
    tb = Globals.intestine_view_tb if Globals.intestine_view_tb else datetime.datetime.now()
    te = Globals.intestine_view_te if Globals.intestine_view_te else tb + datetime.timedelta(days=1)
    
    self.date_filter.set_event_handler(
      "x-period-changed",
      self.date_filter_changed
    )
'''
class IntestineView(IntestineViewTemplate):
  def __init__(
    self,
    main_form=None,
    intestine_form=None,
    **properties
  ):
    super().__init__(**properties)
  
    self.main_form = main_form
    self.intestine_form = intestine_form
  '''
  Така `IntestineView`:  
  main_form       → съществуващият Main
  intestine_form  → старата Intestine инстанция
      self.show_intestine_data(mode, tb, te)
  '''

  
  def date_filter_changed(
    self,
    mode=None,
    tb=None,
    te=None,
    **event_args
  ):
    Globals.intestine_view_mode = mode
    Globals.intestine_view_tb = tb
    Globals.intestine_view_te = te
    
    print(mode, tb, te)  
    self.show_intestine_data(mode, tb, te)


  def show_intestine_data(self, mode, tb, te):
    rows = anvil.server.call(
      "get_intestine_events",
      tb.strftime("%Y-%m-%d" + " 00:00"),    # 
      te.strftime("%Y-%m-%d" + " 00:00")     # + " 23:59"
    )
    self.repeating_panel_1.items = rows


  @handle("back_btn", "click")
  def back_btn_click(self, **event_args):
    # Chain of return:
    self.remove_from_parent()  
    self.main_form.navigation_panel.visible = True  
    self.main_form.content_panel.add_component(
      self.intestine_form
    )




  '''
  @handle("back_btn", "click")
  def back_btn_click(self, **event_args):
    open_form("Intestine")
  '''
