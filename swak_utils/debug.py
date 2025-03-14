from typing import Callable, Optional, Any

# Cool idea, but decorator pretty much does this much easier
def if_debug(DEBUG: bool, function: Callable[..., Optional[Any]], *parameters: Any) -> Optional[Any]:
  """
  **Author:**
  Owen Miller-Fast
  
  **Description:**\n
  Run function passed in function parameter with parameters passed in the parameters parameter if DEBUG is true. Will be developing a decorator to replace this function.
  
  **Parameters:**\n
  *DEBUG:* `bool` - Usually a global variable in python project. True if currently debugging program. False otherwise.\n
  *function:* `Callable[..., Optional[Any]]` - A function that can have no parameters or n parameters of Any type\n
  *\*parameters:* `Any` - List of n parameters for passed function\n

  **Return:**\n
  `Optional[Any]` - It returns whatever the function passed returns. A value/object of any type or nothing.
  """
  
  if DEBUG:
    return function(*parameters)

def debug(debug: bool):
  def decorator_function(orig_func):
    def wrapper_function(*args, **kwargs):
      if debug: return orig_func(*args, **kwargs)
    return wrapper_function
  return decorator_function
