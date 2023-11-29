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
      return(False, f"'{time_str}' НЕ е валиден HH:MM формат")

  
  def validate_dec(self, decimal_str):
    # Regular expression pattern for X.Y format decimal
    decimal_pattern = r'^\d\.\d$'

    # Check if the provided decimal string matches the pattern
    if re.match(decimal_pattern, decimal_str):
        return(True, "")
    else:
        print(f"The decimal '{decimal_str}' is not in a valid X.Y format.")
        return(False, f"'{decimal_str}' НЕ е валиден X.Y формат")

 
    