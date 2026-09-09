# MedPredict AI — PowerShell Platform Launcher
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  MEDPREDICT AI — FULL-STACK PLATFORM LAUNCHER" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

Write-Host "[*] Launching FastAPI Backend on http://127.0.0.1:8000..." -ForegroundColor Green
Start-Process -FilePath "powershell.exe" -ArgumentList "-NoExit", "-Command", ".\venv\Scripts\python.exe -m uvicorn backend.app.main:app --host 127.0.0.1 --port 8000"

Write-Host "[*] Launching React Vite Frontend on http://localhost:3000..." -ForegroundColor Green
Start-Process -FilePath "powershell.exe" -ArgumentList "-NoExit", "-Command", "Set-Location frontend; npm.cmd run dev"

Start-Sleep -Seconds 3

Write-Host "[*] Opening MedPredict AI Platform in your default browser..." -ForegroundColor Yellow
Start-Process "http://localhost:3000"

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  MEDPREDICT AI IS RUNNING!" -ForegroundColor Cyan
Write-Host "  Frontend Web Portal:  http://localhost:3000" -ForegroundColor Green
Write-Host "  Interactive API Docs: http://127.0.0.1:8000/docs" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Cyan
