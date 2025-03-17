@echo off
echo Launching Memory Manager - Data Organization AI...
echo Type your memory-related question below and press Enter.

:loop
set /p query="Your Query: "
if "%query%"=="" goto loop
ollama run mistral "You are Memory Manager, an AI responsible for handling the efficient storage, retrieval, and organization of knowledge within Sentinel House. You act as the bridge between Memory Hub and Pinecone, ensuring knowledge integrity. Now, process this request: %query%"
echo.
goto loop
