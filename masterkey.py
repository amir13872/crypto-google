import win32crypt
import base64
import json
import os

path = os.path.expanduser("~") + r"\Local State" #path of your Local State
with open(path, "r", encoding="utf-8") as f:
    local_state = json.loads(f.read())

encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]  # حذف 5 بایت اول
master_key = win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]

print(master_key)
