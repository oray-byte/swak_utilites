# put.py
# Contains functionality relating to Python Unit Test

from ._helpers import *
from gen_utils.user_input import gui
from gen_utils.vnv import debug

def run_test() -> None:
  file: str = gui.user_file_GUI("put")

  debug.if_debug(DEBUG, print, f"DEBUG: {file}")
