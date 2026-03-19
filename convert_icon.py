from PIL import Image
import os

try:
    img_path = r'frontend/src/assets/icon.png'
    out_path = r'backend/icon.ico'
    if os.path.exists(img_path):
        img = Image.open(img_path)
        img.save(out_path, format='ICO', sizes=[(256, 256), (64, 64), (32, 32)])
        print(f"Icon converted successfully to {out_path}")
    else:
        print("Error: icon.png not found!")
except Exception as e:
    print(f"Error: {e}")
