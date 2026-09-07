import anvil.server
import re
import datetime

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
      return(False, "НЕВАЛИДЕН HH:MM формат")

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
        return(False, "НЕВАЛИДЕН формат") 


  def validate_L(self, value):
    if value in (None, ""):
      return(True, "")

    try:
      value = int(value)
    except:
      return(False, "L трябва да е цяло число")
  
    if 1 <= value <= 60:
      return(True, "")
    else:
      return(False, "L трябва да е между 1 и 60 cm")


  def validate_N(self, value):
    if value in (None, ""):
      return(True, "")
  
    try:
      value = int(value)
    except:
      return(False, "N трябва да е цяло число")
  
    if 1 <= value <= 30:
      return(True, "")
    else:
      return(False, "N трябва да е между 1 и 30")
    