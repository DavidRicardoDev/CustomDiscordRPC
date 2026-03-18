import time
from pypresence import Presence
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RPCManager:
    def __init__(self):
        self.rpc = None
        self.client_id = None
        self.connected = False
        self.start_time = None

    def connect(self, client_id: str):
        if self.connected and self.client_id == client_id:
            return True
        self.disconnect()
        try:
            self.client_id = client_id
            self.rpc = Presence(client_id)
            self.rpc.connect()
            self.connected = True
            logger.info(f"Connected to Discord RPC with client_id: {client_id}")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to Discord RPC: {e}")
            self.connected = False
            return False

    def update(self, **kwargs):
        if not self.connected or not self.rpc:
            return False
            
        # Limpiar keys vacias
        payload = {k: v for k, v in kwargs.items() if v}
        
        try:
            self.rpc.update(**payload)
            logger.info(f"Updated RPC with: {payload}")
            return True
        except Exception as e:
            logger.error(f"Failed to update RPC: {e}")
            self.connected = False
            return False

    def disconnect(self):
        if self.rpc and self.connected:
            try:
                self.rpc.clear()
                self.rpc.close()
            except:
                pass
        self.connected = False
        self.rpc = None

rpc_manager = RPCManager()
