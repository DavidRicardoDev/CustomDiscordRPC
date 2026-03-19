from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from rpc_manager import rpc_manager
import time

global_start_time = None
minimize_to_tray_setting = True
app = FastAPI(title="Discord RPC Customizer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def disable_cache(request, call_next):
    response = await call_next(request)
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

class ConnectRequest(BaseModel):
    client_id: str

class UpdateRequest(BaseModel):
    state: Optional[str] = None
    details: Optional[str] = None
    large_image: Optional[str] = None
    large_text: Optional[str] = None
    small_image: Optional[str] = None
    small_text: Optional[str] = None
    start: Optional[int] = None

@app.post("/api/connect")
def connect_rpc(req: ConnectRequest):
    global global_start_time
    success = rpc_manager.connect(req.client_id)
    if not success:
        raise HTTPException(status_code=400, detail="Fallo de conexión. ¿Discord está abierto?")
    global_start_time = int(time.time())
    return {"status": "connected"}

@app.post("/api/update")
def update_rpc(req: UpdateRequest):
    if not rpc_manager.connected:
        raise HTTPException(status_code=400, detail="No estás conectado al RPC de Discord")
        
    data = req.model_dump(exclude_none=True)
    if global_start_time:
        data["start"] = global_start_time
        
    success = rpc_manager.update(**data)
    if not success:
        raise HTTPException(status_code=400, detail="Fallo al actualizar el RPC. Se perdió la conexión.")
    return {"status": "updated"}

@app.post("/api/disconnect")
def disconnect_rpc():
    rpc_manager.disconnect()
    return {"status": "disconnected"}

@app.get("/api/status")
def get_status():
    return {
        "connected": rpc_manager.connected, 
        "client_id": rpc_manager.client_id,
        "minimize_to_tray": minimize_to_tray_setting
    }

class SettingsRequest(BaseModel):
    minimize_to_tray: bool

@app.post("/api/settings")
def update_settings(req: SettingsRequest):
    global minimize_to_tray_setting
    minimize_to_tray_setting = req.minimize_to_tray
    return {"status": "ok"}
