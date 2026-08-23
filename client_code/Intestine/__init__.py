from ._anvil_designer import IntestineTemplate
from anvil import *
import anvil.server

import datetime

class Intestine(IntestineTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    super().__init__(**properties)

    self.date_picker_1.format = "%Y/%m/%d %H:%M"
    if self.date_picker_1.date is None:
      #self.date_picker_1.date = datetime.datetime.now()
      self.date_picker_1.pick_time = True
      self.date_picker_1.date = datetime.datetime.now()
      self.datetime_box.text = "ДНЕС Е " + self.date_picker_1.date.strftime("%Y-%m-%d %H:%M")[:10] + '      '

    self.validator = validation.Validator(









