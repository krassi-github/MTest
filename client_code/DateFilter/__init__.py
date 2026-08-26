from ._anvil_designer import DateFilterTemplate
from anvil import *
import anvil.server


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

  @handle("D", "clicked")
  def D_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass  # Write Code Here

  @handle("radio_button_2", "clicked")
  def radio_button_2_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass  # Write Code Here

  @handle("radio_button_3", "clicked")
  def radio_button_3_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass  # Write Code Here

  @handle("R", "clicked")
  def R_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass  # Write Code Here

  @handle("prev_btn", "click")
  def prev_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass  # Write Code Here

  @handle("next_btn", "click")
  def next_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass  # Write Code Here

  @handle("period_btn", "click")
  def period_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass  # Write Code Here
