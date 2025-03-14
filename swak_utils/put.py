"""
file: put.py
author: Owen Miller-Fast
description: Contains functionality relating to Python Unit Test
last edited: 03/14/2025 (Owen Miller-Fast)
"""
# Standard imports
from typing import Any, Callable, Dict, Iterable, List, Optional

# Custom imports
import swak_utils.ui as ui
from swak_utils import remove_chars, safe_cast
from swak_utils import debug

DEBUG: bool = True

TYPE_MAP: Dict[str, type] = {
  "int": int,
  "float": float,
  "bool": bool,
  "str": str,
  "Iter": Iterable
}

""" .put file structure
FUNCTION | [INPUTS] | [EXPECTED OUTPUTS]

FUNCTION - Name of the function without the '()'
INPUTS - Semicolon-separated list of inputs that are incapsulated in brackets. Each input needs to have its type listed.
  For a function that requires one string input: [str: Hello];[str: Goodbye];...
  For a function that requires n string inputs: [str: Hello, int: 5, str: No, float: 5.5];[str: Goodbye, int: 55, str: Yes, float: 5.2, ...];...
OUTPUTS - Semicolon-separated list of outputs that are incapsulated in brackets. TODO: Need to have functionality of testing even if no output
  For explanation, see above. Similar to how INPUTS work

TODO: Implement custom types
TODO: Implement Iterables
Types:
Numbers - int
Decimals - float
True/False - bool
Sentences/characters - str
Lists/etc - Iter
"""

class Test_Case:
  test_function: Callable[..., Optional[Any]]
  test_inputs: List[Any]
  test_correct_outputs: List[Any]
  test_outputs: List[Any]

  def __init__(self, function: Callable[..., Optional[Any]], test_inputs: List[Any], test_correct_outputs: List[Any]):
    self.test_function = function
    self.test_inputs = test_inputs
    self.test_correct_outputs = test_correct_outputs

class Test:
  test_cases: List[Test_Case]

  def __init__(self, test_cases=None):
    if test_cases:
      self.test_cases = test_cases

def run_test() -> None:
  file: str = ui.user_file_GUI("put")
  debug.if_debug(DEBUG, print, f"DEBUG: {file}")

# Switched to JSON. It is more popular. Easier use
# """
# Maybe have the parse put parse additional "tests" separated in the file
# """
# def parse_put(put_file: str) -> List[Test]:
#   """
#   **Author:**
#   Owen Miller-Fast
  
#   **Description:**\n
#   Parses .put file.
  
#   **Parameters:**\n
#   *put_file:* `str` - File path of .put file.
#   **Return:**\n
#   None
#   """
#   cases: List[Test_Case]

#   with open(put_file, "r") as file:
#     for line in file:
#       bar_split: List[str] = line.strip().split("|")
#       test_cases: List[Test_Case]
      
#       # Will need to use globals() or locals() to cast string into a callable
#       func: Callable[..., Optional[Any]] = remove_chars(bar_split[0], ["(", ")", " ", "\"", "'"])
#       test_inputs: List[str] = remove_chars(bar_split[1], ["(", ")", " ", "\"", "'"]).strip().split(";")
#       test_outputs: List[str] = remove_chars(bar_split[2], ["(", ")", " ", "\"", "'"]).strip().split(";")
#       for case in test_inputs:
#         case_split: List[str] = case.strip().split(",")
#         true_param: Any
#         for parameter in case_split:
#           # Should only have two elements
#           param_split: List[str] = parameter.strip().split(":")
#           param_type: str = param_split[0]
#           param_value: str = param_split[1]
#           true_param = safe_cast(param_value, TYPE_MAP.get(param_type))

#   unit_test: Test = Test()


def _convert_type(param_type: str):
  type_map = {

  }