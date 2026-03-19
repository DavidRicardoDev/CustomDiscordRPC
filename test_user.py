import sys
import logging
from pypresence import Presence
import time

try:
    client_id = '1483974589141876927'
    rpc = Presence(client_id)
    rpc.connect()
    print("connected")
    # let's try to see if there's any user property
    if hasattr(rpc, 'user'):
        print(f"USER_info: {rpc.user}")
    elif hasattr(rpc, 'client_id'):
        print("has client_id")
        
    print(dir(rpc))    
    rpc.close()
except Exception as e:
    print("error", e)
