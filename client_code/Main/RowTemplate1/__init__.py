from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
from ... import Globals

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.name.text = self.item["name"]
    self.m.text = self.item["morning"]
    self.n.text = self.item["noon"]
    self.e.text = self.item["evening"]
    self.on.text = self.item["on_need"]
