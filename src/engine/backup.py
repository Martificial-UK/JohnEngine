# backup.py
import shutil
import os

def backup_file(src, dest_dir):
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, os.path.basename(src))
    shutil.copy2(src, dest)
    print(f"Backed up {src} to {dest}")
