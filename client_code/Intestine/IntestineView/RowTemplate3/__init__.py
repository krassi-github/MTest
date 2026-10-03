from ._anvil_designer import RowTemplate3Template
from anvil import *
import anvil.server
import datetime


class RowTemplate3(RowTemplate3Template):
  def __init__(self, **properties):
    super().__init__(**properties)

    #self.height = 20
    print("ROW COMPONENTS:")
    for c in self.get_components():
      print(c, type(c))
