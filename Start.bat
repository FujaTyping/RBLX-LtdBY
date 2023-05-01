@echo off
echo Please install python before run this file
where python >nul 2>nul
if %errorlevel% equ 0 (
    echo Detect Python is on this system
) else (
    echo Detect Python is not on this system - Download python from : ^
https://www.python.org/downloads/
)
echo ------------------------------------------
python Main.py
pause