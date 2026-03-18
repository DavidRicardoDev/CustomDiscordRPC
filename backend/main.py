import uvicorn
import webview
import threading
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from api import app
from fastapi.staticfiles import StaticFiles

def start_server():
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="error")

if __name__ == '__main__':
    # Lanzar FastAPI en segundo plano
    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()
    
    if getattr(sys, 'frozen', False):
        # Bundled by PyInstaller
        base_dir = sys._MEIPASS
    else:
        # Development mode
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
    dist_dir = os.path.join(base_dir, 'frontend', 'dist')
    
    if os.path.exists(dist_dir):
        app.mount("/", StaticFiles(directory=dist_dir, html=True), name="static")
        url = "http://127.0.0.1:8000/"
    else:
        # Modo desarrollador: apunta al puerto de Vite
        url = "http://127.0.0.1:5173/"
        
    window = webview.create_window('Discord RPC Customizer', url, width=1024, height=720)
    webview.start()
