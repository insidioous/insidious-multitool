@echo off
REM
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed or not added to PATH. Please install Python.
    pause
    exit /b
)

REM
cd /d "%~dp0"

REM
python tool.py

pause