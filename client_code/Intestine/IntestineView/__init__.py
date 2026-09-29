from ._anvil_designer import IntestineViewTemplate
from anvil import *
import anvil.server


class IntestineView(IntestineViewTemplate):
  def __init__(self, tb, te, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    self.date_filter.set_event_handler(
      "x-period-changed",
      self.date_filter_changed
    )

    self.show_intestine_data(tb, te)

  
  def date_filter_changed(
    self,
    mode=None,
    tb=None,
    te=None,
    **event_args
  ):
    
    print(mode, tb, te)  
    self.show_intestine_data(tb, te)


  def show_intestine_data(self, tb, te):
    rows = anvil.server.call(
      "get_intestine_events",
      tb,
      te
    )
    self.repeating_panel_1.items = rows
