from ._anvil_designer import MainTemplate
from anvil import *
import anvil.js
from .. import Globals


class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.repeating_panel_1.items = [{"name": "T_main", "m": "M2"}]
    '''
    self.is_pwa_on_mobile()
    #
    content_panel = anvil.js.get_dom_node(self.content_panel)
    content_panel.addEventListener('touchstart', self.on_touch_start)
    content_panel.addEventListener('touchmove', self.on_touch_move)
    content_panel.addEventListener('touchend', self.on_touch_end)  
    self.touch_start_y = None
    self.touch_end_y = None    
    # If there is a poll timer
    #if Globals.is_pwa and Globals.is_mobile:
      #self.timer_1.interval = None
    '''

  def refresh_data(self, **event_args):
    ## self.updatestuff_func()
    pass
  def is_pwa_on_mobile(self,**kwargs):
    is_pwa = anvil.js.window.matchMedia("(display-mode: standalone)").matches
    is_mobile = anvil.js.window.navigator.userAgent.lower().find("mobi") > -1
    Globals.is_pwa = is_pwa
    Globals.is_mobile = is_mobile



  # Bunch of handlers
  def on_touch_start(self, event):
    self.touch_start_y = event.touches[0].clientY

  def on_touch_move(self, event):
    self.touch_end_y = event.touches[0].clientY

  def on_touch_end(self, event):
    if self.touch_start_y is not None and self.touch_end_y is not None:
      pull_distance = self.touch_end_y - self.touch_start_y
      if pull_distance > 50:
        self.refresh_data()
    self.touch_start_y = None
    self.touch_end_y = None

  '''My handlers 
  def on_touch_start(self, **event_args):
    pass
  def on_touch_move(self, **event_args):
    pass
  def on_touch_end(self, **event_args):
    pass
  '''
