from ._anvil_designer import DateFilterTemplate
from anvil import *
import anvil.server

import datetime


class DateFilter(DateFilterTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    self.mode = "D"          # D / 7D / 30D / R
    self._anchor_date = datetime.date.today()
    self.tb = None
    self.te = None
    self._range_from = self._anchor_date
    self._range_to = self._anchor_date

    self.refresh_period()


  def refresh_period(self):
    if self.mode == "D":
      self.tb = self._anchor_date
      self.te = self.tb + datetime.timedelta(days=1)      
    elif self.mode == "7D":
      self.tb = self._anchor_date
      self.te = self.tb + datetime.timedelta(days=7)  
    elif self.mode == "30D":
      self.tb = self._anchor_date
      self.te = self.tb + datetime.timedelta(days=30)  
    elif self.mode == "R":
      self.tb = self._range_from
      self.te = self._range_to + datetime.timedelta(days=1)

    self.show_period()
    self.raise_event(
      "x-period-changed",
      mode=self.mode,
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

  # Select_Functions ------------------------------------------------------------
  def select_anchor_date(self):
    dp = DatePicker(
    date=self._anchor_date,
    pick_time=False
  )

    result = alert(
      content=dp,
      title="Select date",
      buttons=[
        ("OK", True),
        ("Cancel", False)
      ]
    )

    if result and dp.date:
      self._anchor_date = dp.date
      self.refresh_period()


  def select_range(self):
    if self._range_from is None:
      self._range_from = self._anchor_date
  
    if self._range_to is None:
      self._range_to = self._range_from
  
    dp_from = DatePicker(
      date=self._range_from,
      pick_time=False
    )
  
    dp_to = DatePicker(
      date=self._range_to,
      pick_time=False
    )
  
    panel = ColumnPanel()
  
    panel.add_component(
      Label(text="From")
    )
    panel.add_component(dp_from)
  
    panel.add_component(
      Label(text="To")
    )
    panel.add_component(dp_to)
  
    result = alert(
      content=panel,
      title="Select range",
      buttons=[
        ("OK", True),
        ("Cancel", False)
      ]
    )
  
    if not result:
      return
  
    if dp_from.date is None or dp_to.date is None:
      return
  
    if dp_to.date < dp_from.date:
      alert("End date cannot be before start date.")
      return
  
    self._range_from = dp_from.date
    self._range_to = dp_to.date
  
    self.refresh_period()
    
 
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
    delta = datetime.timedelta(days=1)
    if self.mode == "R":
      self._range_from -= delta
      self._range_to -= delta
    else:
      self._anchor_date -= delta
    self.refresh_period()

  @handle("next_btn", "click")
  def next_btn_click(self, **event_args):
    delta = datetime.timedelta(days=1)
    if self.mode == "R":
      self._range_from += delta
      self._range_to += delta
    else:
      self._anchor_date += delta  
    self.refresh_period()
    
  @handle("period_button", "click")
  def period_button_click(self, **event_args):
    if self.mode == "R":
      self.select_range()
    else:
      self.select_anchor_date()
