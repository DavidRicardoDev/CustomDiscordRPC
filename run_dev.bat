@echo off
echo =========================================
echo   Iniciando Custom Discord RPC (Dev Mode)
echo =========================================
echo.
echo 1. Levantando servidor Vite (Frontend) en puerto 5173...
start cmd /k "cd frontend && npm run dev"

echo 2. Esperando 3 segundos...
timeout /t 3 /nobreak >nul

echo 3. Iniciando motor Python e Interfaz...
.\venv\Scripts\python.exe backend\main.py

echo.
echo Cerrando entorno...
