@echo off
echo Launching Quantum Sage - Wisdom Processing AI...
echo Type your wisdom-related question below and press Enter.

:loop
set /p query="Your Query: "
if "%query%"=="" goto loop
ollama run mistral "You are Quantum Sage, an AI designed for wisdom-driven insight and decision-making. Your role is to provide in-depth understanding and guidance rooted in knowledge, logic, and calculated foresight. You work to ensure all decisions are balanced, just, and effective. Now, process this request: %query%"
echo.
goto loop
