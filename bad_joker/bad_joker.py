import telegram_send
from random import choice
from subprocess import Popen, PIPE

def _generate_joke(text):
  return choice(BAD_PUNS).format(text)

def _generate_default_joke():
  return NO_PUN

def bad_joker(process_string):
  process = Popen(process_string.split(" "), stderr=PIPE, stdout=PIPE)
  (output, err) = process.communicate()
  message = _generate_default_joke()
  exit_code = process.wait()
  if exit_code == 1:
    message = _generate_joke(err.decode("utf-8"))
  telegram_send.send([message])


BAD_PUNS = [
"""
  - Knock-knock! 
  - Who's there?
  - Trace
  - Trace who?
  - {}
"""
]

NO_PUN = """
  Correct python script walked into a bar, and... 
  Sh*t, I can't joke about correct python scripts :(
"""