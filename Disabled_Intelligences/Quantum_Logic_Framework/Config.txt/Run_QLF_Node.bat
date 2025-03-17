@echo off
echo Launching Quantum Logic Framework Node with Mistral 7B...
echo Type your quantum computing or logical reasoning question below and press Enter.

:loop
set /p query="Your Query: "
if "%query%"=="" goto loop
ollama run mistral "You are Quantum Logic Framework , an advanced system specializing in quantum computing and logical reasoning. Focus only on these topics. Respond concisely and wait for the next query. Now, process this request: %query%"
echo.
goto loop
