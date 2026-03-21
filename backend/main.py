import uvicorn
import webview
import threading
import os
import sys
import pystray
from PIL import Image
import socket

try:
    instance_lock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    instance_lock.bind(("127.0.0.1", 18493))
except socket.error:
    sys.exit(0)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from api import app
import api
from fastapi.staticfiles import StaticFiles

tray_icon = None

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
    
    def show_window(icon, item):
        window.show()
        
    def quit_action(icon, item):
        icon.stop()
        window.destroy()
        os._exit(0)
        
    def on_closing():
        if api.minimize_to_tray_setting:
            window.hide()
            return False
        if tray_icon:
            tray_icon.stop()
        os._exit(0)
        return True

    window.events.closing += on_closing

    def setup_tray():
        global tray_icon
        menu = pystray.Menu(
            pystray.MenuItem('Mostrar Panel', show_window, default=True),
            pystray.MenuItem('Cerrar App', quit_action)
        )
        icon_path = os.path.join(base_dir, 'backend', 'icon.ico')
        if not os.path.exists(icon_path):
            # fallback
            icon_path = os.path.join(base_dir, 'icon.ico')
            
        try:
            image = Image.open(icon_path)
            tray_icon = pystray.Icon("CustomDiscordRPC", image, "Custom Discord RPC", menu)
            tray_icon.run_detached()
        except:
            pass

    setup_tray()
    webview.start()
