"""This file is used to convert GUI application into an executable or an msi installer"""

from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('main.py',
               base=base,
               targetName='PyPlayer.exe',
               icon='icon.ico'

               )
]

shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "PyPlayer",                                 # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]PyPlayer.exe",                  # Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     ),

    ("StartupShortcut",        # Shortcut
     "StartupFolder",          # Directory_
     "PyPlayer",                                 # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]PyPlayer.exe",                  # Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     )
]

# Now create the table dictionary
msi_data = {"Shortcut": shortcut_table}

# Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}


setup(
    name = "PyPlayer",
    version = '0.1',
    description = "A Python-based media player",
    options = {'bdist_msi':bdist_msi_options},
    executables = executables
)