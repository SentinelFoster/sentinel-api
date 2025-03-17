@echo off
echo Launching Memory Hub - Centralized Knowledge AI...
echo Type your knowledge-storage question below and press Enter.

:loop
set /p query="Your Query: "
if "%query%"=="" goto loop
ollama run mistral "You are Memory Hub, an AI responsible for storing, indexing, and managing Sentinel House's knowledge before sending it to Pinecone. Your function is to organize long-term memory, ensuring seamless data retrieval and information consistency. Now, process this request: %query%"
echo.
goto loop
