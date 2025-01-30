import sqlite3
import os
import json
import base64
from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import PBKDF2

def get_encryption_key(master_key):
    return master_key

def decrypt_password(ciphertext, key):
    try:
        # Remove the 'v10' prefix
        iv = ciphertext[3:15]
        encrypted_password = ciphertext[15:-16]
        tag = ciphertext[-16:]

        cipher = AES.new(key, AES.MODE_GCM, iv)
        decrypted_password = cipher.decrypt_and_verify(encrypted_password, tag)
        return decrypted_password.decode()
    except Exception as e:
        return "Error decrypting password"

def fetch_passwords(db_path, master_key):
    key = get_encryption_key(master_key)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
    logins = cursor.fetchall()

    decrypted_logins = []
    for origin_url, username, password in logins:
        decrypted_password = decrypt_password(password, key)
        decrypted_logins.append({
            'url': origin_url,
            'username': username,
            'password': decrypted_password
        })

    conn.close()
    return decrypted_logins

def main(master_key, db_path):
    passwords = fetch_passwords(db_path, master_key)
    for entry in passwords:
        print(f"Site: {entry['url']}")
        print(f"Username: {entry['username']}")
        print(f"Password: {entry['password']}")
        print("-" * 50)

if __name__ == "__main__":
    master_key = b'= \x11\xe0OI\xe0{e\x14[\xadj\xd56\xf7\xe6\xcaO\xe0C\xeb\x8eep\x1b\r\x18\x17\x1dp\xba\xd9'  # Replace with the actual Master Key
    db_path = r"\Desktop\Login Data"
    main(master_key, db_path)
