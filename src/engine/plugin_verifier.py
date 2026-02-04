import hashlib
import os

def verify_plugin_signature(plugin_path, expected_hash):
    with open(plugin_path, "rb") as f:
        data = f.read()
    actual_hash = hashlib.sha256(data).hexdigest()
    return actual_hash == expected_hash
