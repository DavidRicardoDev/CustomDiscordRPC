from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from rpc_manager import rpc_manager

app = FastAPI(title="Discord RPC Customizer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    success = rpc_manager.connect(req.client_id)
    if not success:
        raise HTTPException(status_code=400, detail="Fallo de conexión. ¿Discord está abierto?")
    return {"status": "connected"}

@app.post("/api/update")
def update_rpc(req: UpdateRequest):
    if not rpc_manager.connected:
        raise HTTPException(status_code=400, detail="No estás conectado al RPC de Discord")
    success = rpc_manager.update(**req.model_dump(exclude_none=True))
    if not success:
        raise HTTPException(status_code=400, detail="Fallo al actualizar el RPC. Se perdió la conexión.")
    return {"status": "updated"}

@app.post("/api/disconnect")
def disconnect_rpc():
    rpc_manager.disconnect()
    return {"status": "disconnected"}

@app.get("/api/status")
def get_status():
    return {"connected": rpc_manager.connected, "client_id": rpc_manager.client_id}
