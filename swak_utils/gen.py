from typing import Any, List

def safe_cast(value: Any, to_type: type) -> Any:
  try:
    return to_type(value)
  except ValueError:
    print(f"Failed to cast {value} to {to_type}")
    return None
  
def remove_chars(string: str, characters: List[str]) -> str:
  # Check that each str in characters is only len. one. Must be single characters
  if any(len(char) > 1 for char in characters): raise ValueError("Must only be characters in characters parameters")

  modified_string: str = string

  for char in characters:
    modified_string = "".join(modified_string.split(char))
  
  return modified_string