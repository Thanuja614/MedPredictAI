@echo off
title MedPredict AI — Master Platform Launcher
echo ============================================================
echo   MEDPREDICT AI — FULL-STACK PLATFORM LAUNCHER
echo ============================================================
echo [*] Starting FastAPI Backend on http://127.0.0.1:8000 ...
start "MedPredict Backend" cmd /k ".\venv\Scripts\python.exe -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000"

echo [*] Starting React Frontend on http://localhost:3000 ...
start "MedPredict Frontend" cmd /k "cd frontend && npm.cmd run dev"

echo [*] Waiting 3 seconds for services to initialize...
timeout /t 3 /nobreak >nul

echo [*] Opening MedPredict AI Platform in your default browser...
start http://localhost:3000

echo ============================================================
echo   MEDPREDICT AI IS RUNNING!
echo   Frontend Web Portal:  http://localhost:3000
echo   Interactive API Docs: http://127.0.0.1:8000/docs
echo ============================================================
