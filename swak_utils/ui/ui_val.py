from typing import Any, Iterable

def validate_YNinput(prompt: str) -> str:
  """
  **Author:**
  Owen Miller-Fast
  
  **Description:**\n
  Validates user input with Y or N choices. Ensures either a Y/y or a N/n answer. The function appends '[Y/N]: ' to the end of the prompt parameter.
  
  **Parameters:**\n
  *prompt:* `str` - The prompt string wanted to be used in the `input()` function.
  
  **Return:**\n
  `str` - The reponse to the prompt in lowercase. 'y' or 'n'.
  """
  
  user_input: str = input(f"{prompt} [Y/N]: ")

  is_y = user_input.lower() == "y"
  is_n = user_input.lower() == "n"

  while((is_y and not is_n) and (is_n and not is_y)):
    user_input: str = input(f"{prompt} [Y/N]: ")

    is_y = user_input.lower() == "y"
    is_n = user_input.lower() == "n"

  return user_input.lower()

def validate_num_input(input: Iterable[Any], max: int, min: int=1):
  if min < 1:
    raise ValueError("Invalid value provided: parameter min must be at least 1")
  
  if min > max:
    raise ValueError("Invalid value provided: parameter max must be greater than or equal to parameter min")
  
  if not isinstance(input, Iterable):
    raise TypeError("Invalid type provided: parameter input must be of type Iterable")
  
  input_len: int = len(input)  
  is_in_bounds: bool = (input_len >= min and input_len <= max)

  return is_in_bounds