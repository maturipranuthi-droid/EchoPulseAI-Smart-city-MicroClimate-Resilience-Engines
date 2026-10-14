@echo off
echo ========================================================
echo       EcoPulse.AI - Smart City Resilience Engine
echo ========================================================
echo.

echo [1/2] Starting FastAPI Backend on http://localhost:8000...
start "EcoPulse Backend" cmd /k "cd backend && .venv\Scripts\python.exe -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload"

echo [2/2] Starting Next.js Frontend on http://localhost:3000...
start "EcoPulse Frontend" cmd /k "cd frontend && npm run dev"

echo.
echo ========================================================
echo EcoPulse.AI is launching!
echo Frontend: http://localhost:3000
echo Backend API Docs: http://localhost:8000/docs
echo ========================================================
pause
