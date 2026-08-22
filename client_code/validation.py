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
      return(False, f"НЕВАЛИДЕН HH:MM формат")

  # Datetime format YYYY/MM/DD HH:MM     22-08-2026
  def validate_datetime(self, datetime_str):
    datetime_pattern = r'^\d{4}/\d{2}/\d{2} ([0-1][0-9]|2[0-3]):[0-5][0-9]$'

    if not re.match(datetime_pattern, datetime_str):
      return(False, "НЕВАЛИДЕН YYYY/MM/DD HH:MM формат")

    try:
      datetime.datetime.strptime(datetime_str, "%Y/%m/%d %H:%M")
      return(True, "")
    except ValueError:
      return(False, "НЕВАЛИДНА дата или час")

  
  def validate_pcs(self, input_str):
    # Regular expression pattern for X.Y format decimal or one-digit integer
    decimal_integer_pattern = r'^(\d\.\d|\d)$'

    # Check if the provided string matches the pattern
    if re.match(decimal_integer_pattern, input_str):
        return(True, "")
    else:
        return(False, f"НЕВАЛИДЕН формат") 
    