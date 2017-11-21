import cx_Freeze
import sys
import docx

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("Main.py", base=base, icon="DC.ico")]

cx_Freeze.setup(
    name="DC",
    options={"build_exe": {"packages": ["tkinter", "docx"], "include_files": ["DC.ico"]}},
    version="0.01",
    executables=executables
)
