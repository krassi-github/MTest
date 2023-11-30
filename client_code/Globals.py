import anvil.server
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#
is_pwa = False
is_mobile = False

status = []
# status FORMAT
'''    s = {"p_id": r[p_id], "name": r[name], "code": r[r_m_code], "morning": r[morning],
         "m_ex": False, "noon": r[noon], "n_ex": False, "evening": r[evening],
         "e_ex": False, "on_need": r[on_need], "on_ex": False}'''
#Intake data format:
#int_id	time	m_code	det_code	type	pcs	note


intake_time = ""
intake_code = "" 
intake_pcs = 0.0
intake_type = ""
intake_notes = ""

def load_data(date):
  global status  
  r, status = anvil.server.call("get_status", date)
  return(r)


def get_med_name(med_code):
  global status
  for i in range(len(status)):
    if med_code == status[i]["code"]:
      return(status[i]["name"])
  return("---")


def get_pcs_type(med_code, time):
  global status, intake_code, intake_type
  r = -1.0
  t = "-"
  for i in range(len(status)):
    if med_code == status[i]["code"]:
      intake_code = status[i]["code"]
      if time == "m":
        r = status[i]["morning"]
        t = "сутрин"
        intake_type = "morning"
      elif time == "n":
        r = status[i]["noon"]
        t = "обед"
        intake_type = "noon"
      elif time == "e":
        r = status[i]["evening"]
        t = "вечер"
        intake_type = "evening"
      elif time == "on_need":
        r = status[i]["on"]
        t = "при нужда"
        intake_type = "on_need"
      else:
        anvil.server.call("mh_log", -401, f"get_med_pcs() Invalid time= {time}")
  return(r, t)
      

def put_intake():
  global intake_time, intake_pcs, intake_type, intake_notes, status
  
  date = anvil.server.call("get_time")
  # parameters list: time, m_code, type, pcs, notes 
  r = anvil.server.call("put_intake", date[:10]+' '+intake_time, intake_code, \
                        intake_type, intake_pcs, intake_notes)
  return(r)

  