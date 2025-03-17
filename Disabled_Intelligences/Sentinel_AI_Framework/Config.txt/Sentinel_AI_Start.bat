@echo off
echo Launching Sentinel AI Framework with Mistral 7B...
echo Type your AI-related question below and press Enter.

:loop
set /p query="Your Query: "
if "%query%"=="" goto loop
ollama run mistral "You are Sentinel AI Framework, an advanced artificial intelligence system. Focus only on AI-related topics. Respond concisely and wait for the next query. Now, process this request: %query%"
echo.
goto loop
