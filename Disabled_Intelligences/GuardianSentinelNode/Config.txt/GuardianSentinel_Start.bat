@echo off
echo Launching Guardian Sentinel with Mistral 7B...
echo Loading configuration...

:: Check if config.txt exists
if not exist config.txt (
    echo ERROR: Configuration file missing! Guardian Sentinel cannot launch.
    pause
    exit
)

:: Read the config.txt content
setlocal enabledelayedexpansion
set "config_content="
for /f "delims=" %%A in (config.txt) do set "config_content=!config_content! %%A"

echo Type your cybersecurity question below and press Enter.

:loop
set /p query="Your Query: "
if "%query%"=="" goto loop
ollama run mistral "!config_content! Now, process this request: %query%"
echo.
goto loop
