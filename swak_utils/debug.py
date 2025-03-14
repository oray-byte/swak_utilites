"""
file: debug.py
author: Owen Miller-Fast (oray-byte)
description: Debugging utilities for python projects
last edited: 03/14/2025 (Owen Miller-Fast)
"""

from typing import Optional, Any, Dict, Tuple

# global variables
DEBUG: bool = True

# Cool idea, but decorator pretty much does this much easier
def debug_wrapper(function: Any, *args: Tuple, **kwargs: Dict[str, Any]) -> Optional[Any]:
  """
  **Author:**
  Owen Miller-Fast
  
  **Description:**\n
  Run function passed in function parameter with parameters passed in the parameters parameter if DEBUG is true. Useful for predefined functions
  
  **Parameters:**\n
  *DEBUG:* `bool` - Usually a global variable in python project. True if currently debugging program. False otherwise.\n
  *function:* `Callable[..., Optional[Any]]` - A function that can have no parameters or n parameters of Any type\n
  *\*parameters:* `Any` - List of n parameters for passed function\n

  **Return:**\n
  `Optional[Any]` - It returns whatever the function passed returns. A value/object of any type or nothing.
  """
  
  if DEBUG:
    return function(*args, **kwargs)
  else:
    return None

def debug(orig_func):
  def wrapper_function(*args, **kwargs):
    if DEBUG: return orig_func(*args, **kwargs)
  return wrapper_function
