import anvil.server
import re


class Validator():

  def __init__(self):
    pass

  # Time format HH:MM
  def validate_time(self, time_str):
    # Regular expression pattern for HH:MM format
    time_pattern = r'^([0-1][0-9]|2[0-3]):([0-5][0-9])$'
  
    # Check if the provided time string matches the pattern
    if re.match(time_pattern, time_str):
      return(True)
    else:
      return(False, f"The time '{time_str}' is not in a valid HH:MM format")

 
    
  def require(self, component, event_list, predicate, error_lbl=None, show_errors_immediately=False):
    def check_this_component(**e):
      result = predicate(component)
      self._validity[component] = result
      if error_lbl is not None:
        error_lbl.visible = not result
      self._check()
      
    for e in event_list:
      component.set_event_handler(e, check_this_component)
    self._component_checks.append(check_this_component)
      
    if show_errors_immediately:
      check_this_component()
    else:
      # By default, won't show the error until the event triggers,
      # but we will (eg) disable buttons
      if error_lbl is not None:
        error_lbl.visible = False
      self._validity[component] = predicate(component)
      self._check()
   
  def require_text_field(self, text_box, error_lbl=None, show_errors_immediately=False):
    self.require(text_box, ['change', 'lost_focus'],
                 lambda tb: tb.text not in ('', None),
                 error_lbl, show_errors_immediately)
        
  def require_checked(self, check_box, error_lbl=None, show_errors_immediately=False):
    self.require(check_box, ['change'],
                 lambda cb: cb.checked,
                 error_lbl, show_errors_immediately)
      
  def enable_when_valid(self, component):
    def on_change(is_valid):
      component.enabled = is_valid
    self._actions.append(on_change)
    self._check()

  def is_valid(self):
    """Return True if this form is valid, False if it's not."""
    return all(self._validity.values())
  
  def show_all_errors(self):
    """Run all component checks and perform the appropriate actions if any fields are invalid."""
    for check_component in self._component_checks:
      check_component()
    
  def _check(self):
    v = self.is_valid()
    for f in self._actions:
      f(v)
