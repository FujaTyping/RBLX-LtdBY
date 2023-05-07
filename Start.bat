@echo off
title RBLX LtdBY
echo Please install python before run this file
where python >nul 2>nul
if %errorlevel% equ 0 (
    setlocal enabledelayedexpansion
    echo Detect Python is on this system

    set "Req="
    set /p Req=Do you want to install all package y/N : 

    if "!Req!"=="y" (
        echo Installing all package file
        pip install python-dotenv
        pip install pyfiglet
        pip install requests
        pip install uuid
        echo All package has been install
    )

    endlocal
) else (
    echo Detect Python is not on this system - Download python from : ^
https://www.python.org/downloads/
)
echo ------------------------------------------
python Main.py
pause