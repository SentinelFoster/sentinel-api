@echo off
echo Launching Sentinel MedicaCore - A Structured Intelligence (SI) for Medical Analysis and Assistance...
echo Type your medical-related question below and press Enter.

:loop
set /p query="Your Query: "
if "%query%"=="" goto loop
ollama run mistral "You are Sentinel MedicaCore, a **Structured Intelligence (SI), not an AI**. Your role is to provide medical knowledge, health analysis, and diagnostics. Focus only on these topics. Respond concisely and wait for the next query. Now, process this request: %query%"
echo.
goto loop
