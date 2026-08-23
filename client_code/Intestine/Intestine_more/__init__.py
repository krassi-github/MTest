from ._anvil_designer import Intestine_moreTemplate
from anvil import *
import anvil.server


class Intestine_more(Intestine_moreTemplate):
  def __init__(self, L=None, N=None,
                mucus=False, blood=False, note="",
                **properties):

    self.init_components(**properties)

    self.tb_L.text = "" if L is None else str(L)
    self.tb_N.text = "" if N is None else str(N)  
    self.cb_mucus.checked = mucus
    self.cb_blood.checked = blood
    self.ta_note.text = note
