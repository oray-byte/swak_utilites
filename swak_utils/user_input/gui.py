import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from typing import List, Optional

def user_directory_GUI() -> None:
  """
  **Author:**
  Owen Miller-Fast
  
  **Description:**\n
  Opens GUI to choose directory
  
  **Parameters:**\n
  None
  
  **Return:**\n
  `str` - Name of choosen directory
  """
  
  root: tk.Tk = tk.Tk()
  root.withdraw()

  directory: str = fd.askdirectory(title="Select Desired Directory")

  while not directory:
    mb.showwarning("Alert", "Must choose a directory.")
    directory = fd.askdirectory(title="Select Desired Directory")
  
  return directory

def user_file_GUI(default_ext: str) -> str:
  """
  **Author:**
  Owen Miller-Fast
  
  **Description:**\n
  Opens GUI to choose file
  
  **Parameters:**\n
  *default_ext:* `str` - The extension of the file you are wanting the user to use\n
  *filetypes:* `List[str] | None` - List of additional file types that can be used. Defaults to none.\n
  
  **Return:**\n
  `str` - The name of the file to be opened. This function doesn't open the file itself
  """
  
  root: tk.Tk = tk.Tk()
  root.withdraw()


  file: str = fd.askopenfilename(filetypes=[(f".{default_ext} files", f"*.{default_ext}")])

  while not file:
    mb.showwarning("Alert", f"Must choose a .{default_ext} file.")
    file: str = fd.askopenfilename(filetypes=[(f".{default_ext} files", f"*.{default_ext}")])

  return file
