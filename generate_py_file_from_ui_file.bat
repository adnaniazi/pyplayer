REM This batch file when executed converts the .ui file into a .py file. 
@echo off
call pyuic4 -x my_gui.ui -o my_gui.py