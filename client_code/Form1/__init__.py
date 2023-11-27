from ._anvil_designer import Form1Template
from anvil import *
import anvil.js
from .. import Globals


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.is_pwa_on_mobile()
    #
    content_panel = anvil.js.get_dom_node(self.content_panel)
    content_panel.addEventListener('touchstart', self.on_touch_start)
    content_panel.addEventListener('touchmove', self.on_touch_move)
    content_panel.addEventListener('touchend', self.on_touch_end)

    self.touch_start_y = None
    self.touch_end_y = None


  def is_pwa_on_mobile(self,**kwargs):
    is_pwa = anvil.js.window.matchMedia("(display-mode: standalone)").matches
    is_mobile = anvil.js.window.navigator.userAgent.lower().find("mobi") > -1
    Globals.is_pwa = is_pwa
    Globals.is_mobile = is_mobile



  # Bunch of handlers
  def on_touch_start(self, **event_args):
    pass
  def on_touch_move(self, **event_args):
    pass
  def on_touch_end(self, **event_args):
    pass
    
