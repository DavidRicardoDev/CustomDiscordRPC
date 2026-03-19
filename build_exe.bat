@echo off
echo =========================================
echo   Compilando Custom Discord RPC para Prod
echo =========================================
echo.
echo 1. Compilando Vue (Frontend)...
cd frontend
call npm run build
if %ERRORLEVEL% NEQ 0 (
    echo Error compilando el Frontend.
    pause
    exit /b %ERRORLEVEL%
)
cd ..

echo.
echo 2. Empaquetando Python y Recursos...
.\venv\Scripts\pyinstaller.exe --onefile --noconsole --icon="backend/icon.ico" --name "Custom Discord RPC" --add-data "frontend/dist;frontend/dist" --add-data "backend/icon.ico;backend" backend/main.py
if %ERRORLEVEL% NEQ 0 (
    echo Error durante PyInstaller.
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo COMPILACION EXITOSA! Tu nuevo .exe esta en la carpeta "dist".
pause
