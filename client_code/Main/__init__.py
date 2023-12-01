from ._anvil_designer import MainTemplate
from anvil import *
import anvil.server
import anvil.js
from anvil.js import window
from .. import Globals

# status FORMAT
'''    s = {"p_id": r[p_id], "name": r[name], "code": r[r_m_code], "morning": r[morning],
         "m_ex": False, "noon": r[noon], "n_ex": False, "evening": r[evening],
         "e_ex": False, "on_need": r[on_need], "on_ex": False}'''


class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

    #self.row_spacing = 0
    #self.repeating_panel_1.row_spacing = 0
    self.date.text = anvil.server.call("get_time")[:10]
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
      
    self.refresh_data()

  def refresh_data(self, **event_args):
    date = anvil.server.call("get_time")
    r = Globals.load_data(date)
    self.repeating_panel_1.items = Globals.status
    # self.dgnst.text = Globals.status
    if r < 0:
      self.date.text = f"PROBLEM {r}"
      self.date.foreground = red   
    
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
