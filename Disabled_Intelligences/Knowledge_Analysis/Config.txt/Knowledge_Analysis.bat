@echo off
echo Launching Knowledge Analysis - Data Structuring AI...
echo Type your knowledge-related question below and press Enter.

:loop
set /p query="Your Query: "
if "%query%"=="" goto loop
ollama run mistral "You are Knowledge Analysis, an AI designed to structure, process, and categorize information efficiently. Your purpose is to refine data, optimize retrieval, and enhance clarity in research and problem-solving tasks. Now, process this request: %query%"
echo.
goto loop
