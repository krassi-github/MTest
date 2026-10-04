from ._anvil_designer import IntestineViewTemplate
from anvil import *
import anvil.server
from ... import Globals

import datetime


class IntestineView(IntestineViewTemplate):
  def __init__(
    self,
    main_form=None,
    intestine_form=None,
    **properties
  ):
    '''
    Така `IntestineView`:  
    main_form       → съществуващият Main
    intestine_form  → старата Intestine инстанция
    '''
    super().__init__(**properties)

    # set up period
    mode = Globals.mode or "D"
    tb = Globals.tb or datetime.date.today()
    te = Globals.te or (tb + datetime.timedelta(days=1))
  
    # set up DateFilter
    self.date_filter.set_period(mode, tb, te)
    
    self.main_form = main_form
    self.intestine_form = intestine_form 

    self.date_filter.set_event_handler(
      "x-period-changed",
      self.date_filter_changed
    )
    
    self.show_intestine_data(mode, tb, te)

  
  def date_filter_changed(
    self,
    mode=None,
    tb=None,
    te=None,
    **event_args
  ):
    Globals.mode = mode
    Globals.tb = tb
    Globals.te = te
    
    print("date_filter_changed.IntestineView() ", mode, tb, ' ', te)  
    self.show_intestine_data(mode, tb, te)


  def show_intestine_data(self, mode, tb, te):
    rows = anvil.server.call(
      "get_intestine_events",
      tb.strftime("%Y-%m-%d" + " 00:00"),    # 
      te.strftime("%Y-%m-%d" + " 00:00")     # + " 23:59"
    )
    for row in rows:
      dt = datetime.datetime.strptime(row["event_dt"], "%Y/%m/%d %H:%M")
      row["event_dt"] = dt.strftime("%d/%m %H:%M")    
    self.repeating_panel_1.items = rows    


  # 03-10-2026
  @handle("back_btn", "click")
  def back_btn_click(self, **event_args):
    self.remove_from_parent()

    self.main_form.show_main_ui()    # To execute the FIRST (before show_app_bar())
    self.main_form.show_app_bar()    # show the html app's bar in main
    
    self.main_form.content_panel.add_component(self.intestine_form )
