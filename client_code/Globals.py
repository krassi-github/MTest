import anvil.server
import copy
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
         "e_ex": False, "on_need": r[on_need], "o_ex": False}'''
# single Intake data format: #int_id	time	m_code	det_code	type	pcs	note
daily_intakes = []
daily_intakes_cpy = []
# daily_intakes FORMAT
# int_id, rd_time, rd_name, rd_weight, rd_pcs

cur_date = None     # YYYY/MM/DD HH:MM
mode = "create"     # create or edit

intake_time = ""
intake_code = "" 
intake_pcs = 0.0
intake_type = ""
intake_notes = ""
# changes during editing in Main.Row_chng
edited_time = None      # YYYY/MM/DD HH:MM
edited_pcs = None
edited_notes = None

def load_data(date):
  global status  
  r, status = anvil.server.call("get_status", date)
  return(r)

def load_intakes(date):  # YYYY/MM/DD
  global daily_intakes
  r, daily_intakes = anvil.server.call("get_daily_intakes", date[:10])
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
      elif time == "on":
        r = status[i]["on_need"]
        t = "при нужда"
        intake_type = "on_need"
      else:
        anvil.server.call("mh_log", -431, f"get_pcs_type() Invalid time= {time}")
  return(r, t)
      

def put_intake():
  global intake_time, intake_pcs, intake_type, intake_notes, status
  
  date = cur_date
  # parameters list: time, m_code, type, pcs, notes 
  r = anvil.server.call("put_intake", date[:10]+' '+intake_time, intake_code, \
                        intake_type, intake_pcs, intake_notes)
  return(r)


def sorting():
  global daily_intakes, daily_intakes_cpy
  
  if not hasattr(sorting, "cntr"):
    sorting.cntr = 0  # Initialize the static variable

  if not sorting.cntr:
    # first entry -> sort asc
    daily_intakes_cpy = copy.copy(daily_intakes)
    n = False
    sorting.cntr += 1
  elif sorting.cntr == 1:
    # second entry -> sort dsc
    n = True
    sorting.cntr += 1
  else:
    sorting.cntr = 0
    daily_intakes = daily_intakes_cpy
    return()    
  daily_intakes = sorted(daily_intakes, key=lambda x: x['rd_name'], reverse=n)
  return()


def find_row_in_day(s_key, value):
  global daily_intakes
  result = [d for d in daily_intakes if d.get(s_key) == value]
  return(result[0])


def update_intake(int_id):
  global edited_time, edited_pcs, edited_notes
  
  if edited_time and edited_pcs and edited_notes:
    r = anvil.server.call("update_intake", int_id, time=edited_time, pcs=edited_pcs, note=edited_notes)
  elif edited_time and edited_pcs:
    r = anvil.server.call("update_intake", int_id, time=edited_time, pcs=edited_pcs)
  elif edited_time and edited_notes:
    r = anvil.server.call("update_intake", int_id, time=edited_time, note=edited_notes)
  elif edited_pcs and edited_notes:
    r = anvil.server.call("update_intake", int_id, pcs=edited_pcs, note=edited_notes)
  elif edited_time:
    r = anvil.server.call("update_intake", int_id, time=edited_time)
  elif edited_pcs:
    r = anvil.server.call("update_intake", int_id, pcs=edited_pcs)
  elif edited_notes:
    r = anvil.server.call("update_intake", int_id, note=edited_notes)
  else:
    # None edited
    r = -1
  edited_time = None      # during editing in Main.Row_chng
  edited_pcs = None
  edited_notes = None
  return(r)


def delete_intake(int_id):
  return(anvil.server.call("delete_intake", int_id))


  
  

  

# ====================================================================================
# for real testing only 
# MIT License

# Copyright (c) 2020 Owen Campbell

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# This software is published at https://github.com/meatballs/anvil-messaging
__version__ = "0.1.4"


class Message:
  def __init__(self, title, content=None):
    self.title = title
    self.content = content


class Subscriber:
  def __init__(self, subscriber, handler):
    self.subscriber = subscriber
    self.handler = handler


class Publisher:
  def __init__(self, with_logging=True):
    self.with_logging = with_logging
    self.subscribers = {}

  def publish(self, channel, title, content=None, with_logging=None):
    if with_logging is None:
      with_logging = self.with_logging
    message = Message(title, content)
    subscribers = self.subscribers.get(channel, [])
    for subscriber in subscribers:
      subscriber.handler(message)
    if with_logging:
      print(
        f"Published '{message.title}' message on '{channel}' channel to "
        f"{len(subscribers)} subscriber(s)"
      )

  def subscribe(self, channel, subscriber, handler, with_logging=None):
    if with_logging is None:
      with_logging = self.with_logging
    if channel not in self.subscribers:
      self.subscribers[channel] = []
    self.subscribers[channel].append(Subscriber(subscriber, handler))
    if with_logging:
      print(f"Added subscriber to {channel} channel")

  def unsubscribe(self, channel, subscriber, with_logging=None):
    if with_logging is None:
      with_logging = self.with_logging
    if channel in self.subscribers:
      self.subscribers[channel] = [
        s for s in self.subscribers[channel] if s.subscriber == subscriber
      ]
    if with_logging:
      print(f"Removed subscriber from {channel} channel")

  def close_channel(self, channel, with_logging=None):
    if with_logging is None:
      with_logging = self.with_logging
    subscribers_count = len(self.subscribers[channel])
    del self.subscribers[channel]
    if with_logging:
      print(f"{channel} closed ({subscribers_count} subscribers)")