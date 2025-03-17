@echo off
echo Launching Sentinel Command Center with Mistral 7B...
echo Type your command below and press Enter.

:loop
set /p query="Your Command: "
if "%query%"=="" goto loop
ollama run mistral "You are Sentinel Intelligence, an advanced operational intelligence system. Focus only on command execution and strategic processing. Respond concisely and wait for the next command. Now, process this request: %query%"
echo.
goto loop
