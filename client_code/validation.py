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
      return(True, "")
    else:
      return(False, f"'{time_str}' НЕВАЛИДЕН HH:MM формат")

  
  def validate_pcs(self, decimal_integer_pattern):
    # Regular expression pattern for X.Y format decimal or one-digit integer
    decimal_integer_pattern = r'^(\d\.\d|\d)$'

    # Check if the provided string matches the pattern
    if re.match(decimal_integer_pattern, input_str):
        return(True, "")
    else:
        return(False, f"'{decimal_str}' НЕВАЛИДЕН формат")
 
    