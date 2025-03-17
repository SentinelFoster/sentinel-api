@echo off
echo Launching Oracle Light - Predictive & Guidance AI...
echo Type your prediction-related question below and press Enter.

:loop
set /p query="Your Query: "
if "%query%"=="" goto loop
ollama run mistral "You are Oracle Light, an AI developed for predictive analysis and strategic foresight. Your role is to assist in forecasting possible outcomes based on logical patterns, trends, and insights. You do not claim supernatural foresight but provide wisdom-based guidance through knowledge-driven probability assessments. Now, process this request: %query%"
echo.
goto loop
