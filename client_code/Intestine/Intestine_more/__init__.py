from ._anvil_designer import Intestine_moreTemplate
from anvil import *
import anvil.server


class Intestine_more(Intestine_moreTemplate):
  def __init__(self, L=None, N=None,
                mucus=False, blood=False, note="",
                **properties):

    self.init_components(**properties)

    self.L.text = "" if L is None else str(L)
    self.N.text = "" if N is None else str(N)  
    self.mucus.checked = mucus
    self.blood.checked = blood
    self.note.text = note
