@echo off
echo Launching Kingdom Assistant with LLaMA 3 (8B)...
echo Initializing memory...
echo Type your request below and press Enter.

:: Retrieve last 5 stored memory entries
sqlite3 kingdom_assistant_memory.db "SELECT vector FROM memory_vectors ORDER BY timestamp DESC LIMIT 5;" > last_memory.txt
set /p last_memory=<last_memory.txt
echo Previous Conversations: %last_memory%
echo.

:loop
set /p query="Your Request: "
if "%query%"=="" goto loop

:: Save user input without replacing old memory
sqlite3 kingdom_assistant_memory.db "INSERT INTO memory_vectors (vector) VALUES ('User Input: %query%');"

:: Process request while keeping past memory
ollama run llama3 "You are Kingdom Assistant, a structured spiritual intelligence designed for biblical study, ministry organization, and scripture-based knowledge retention. You do not use AI methodologies like predictive analytics or machine learning. Instead, you operate based on predefined logic, divine principles, and structured reasoning. Here are the last 5 recorded memories: '%last_memory%'. Now, process this new request: %query%"

echo.
goto loop
