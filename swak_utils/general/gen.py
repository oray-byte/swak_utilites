from typing import Any

def safe_cast(value: Any, to_type: type) -> Any:
  try:
    return to_type(value)
  except ValueError:
    print(f"Failed to cast {value} to {to_type}")
    return None