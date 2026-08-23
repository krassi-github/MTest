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
      self.msg_box.text = timefstr









# self.b_room_b.role = "elevated-button"

  @handle("date_picker_1", "show")
  def date_picker_1_show(self, **event_args):
    c = DatePicker(format="%d %m %Y")

    # Set to a datetime.datetime
    c.pick_time = True
    c.date = datetime.datetime.now()