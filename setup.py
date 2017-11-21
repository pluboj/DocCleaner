import cx_Freeze
import sys
import docx

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("Main.py", base=base)]

cx_Freeze.setup(
    name="DC",
    options={"build_exe": {"packages": ["tkinter", "docx"]}},
    version="0.01",
    executables=executables
)
