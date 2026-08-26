from ._anvil_designer import DateFilterTemplate
from anvil import *
import anvil.server

import datetime


class DateFilter(DateFilterTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    self.mode = "D"          # D / 7D / 30D / R
    self.anchor_date = ...
    self.tb = ...
    self.te = ...
    self.range_from = None
    self.range_to = None


  def refresh_period(self):
    if self.mode == "D":
      self.tb = self.anchor_date
      self.te = self.tb + datetime.timedelta(days=1)      
    elif self.mode == "7D":
      self.tb = self.anchor_date
      self.te = self.tb + datetime.timedelta(days=7)  
    elif self.mode == "30D":
      self.tb = self.anchor_date
      self.te = self.tb + datetime.timedelta(days=30)  
    elif self.mode == "R":
      self.tb = self.range_from
      self.te = self.range_to + datetime.timedelta(days=1)

    self.show_period()
    self.raise_event(
    "x-period-changed",
    tb=self.tb,
    te=self.te
  )


  def show_period(self):
    if self.mode == "D":
      self.period_button.text = self.tb.strftime("%d/%m")

    else:
      last_day = self.te - datetime.timedelta(days=1)
  
      self.period_button.text = (
        self.tb.strftime("%d/%m") +
        " - " +
        last_day.strftime("%d/%m")
    )
  
  # Radio buttons ------------------------------------------------
  @handle("rb_d", "change")
  def rb_d_change(self, **event_args):
    if self.rb_d.selected:
      self.mode = "D"
      self.refresh_period()
  
  @handle("rb_7d", "change")
  def rb_7d_change(self, **event_args):
    if self.rb_7d.selected:
      self.mode = "7D"
      self.refresh_period()
  
  @handle("rb_30d", "change")
  def rb_30d_change(self, **event_args):
    if self.rb_30d.selected:
      self.mode = "30D"
      self.refresh_period()
  
  @handle("rb_range", "change")
  def rb_range_change(self, **event_args):
    if self.rb_range.selected:
      self.mode = "R"
      self.select_range()
  
 
  # Buttons  --------------------------------------------------------
  @handle("prev_btn", "click")
  def prev_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass  # Write Code Here

  @handle("next_btn", "click")
  def next_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass  # Write Code Here

  @handle("period_button", "click")
  def period_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass  # Write Code Here
