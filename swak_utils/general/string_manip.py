# manipulation.py
from typing import List

def remove_chars(string: str, characters: List[str]) -> str:
  # Check that each str in characters is only len. one. Must be single characters
  if any(len(char) > 1 for char in characters): raise ValueError("Must only be characters in characters parameters")

  modified_string: str = string

  for char in characters:
    modified_string = "".join(modified_string.split(char))
  
  return modified_string