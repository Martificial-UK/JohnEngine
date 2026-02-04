import threading

class ConfigReloader:
    def __init__(self, config_path, on_reload=None, interval=5):
        self.config_path = config_path
        self.on_reload = on_reload
        self.interval = interval
        self._last_mtime = None
        self._stop = False
        self._thread = threading.Thread(target=self._watch, daemon=True)

    def start(self):
        self._thread.start()

    def stop(self):
        self._stop = True
        self._thread.join()

    def _watch(self):
        import time
        while not self._stop:
            try:
                mtime = os.path.getmtime(self.config_path)
                if self._last_mtime is None or mtime != self._last_mtime:
                    self._last_mtime = mtime
                    config = load_config(self.config_path)
                    if self.on_reload:
                        self.on_reload(config)
            except Exception as e:
                handle_error(e, context="Config hot-reload")
            time.sleep(self.interval)
def validate_input(data, allowed_types=(str, int, float, bool), max_length=10000, allow_none=False):
    """Enhanced input validation utility."""
    if data is None and not allow_none:
        raise ValueError("Input cannot be None")
    if not isinstance(data, allowed_types):
        raise ValueError(f"Invalid input type: {type(data)}")
    if isinstance(data, str) and len(data) > max_length:
        raise ValueError(f"Input string too long: {len(data)} > {max_length}")
    return True
class Metrics:
    def __init__(self):
        self.data = {}
    def inc(self, key, amount=1):
        self.data[key] = self.data.get(key, 0) + amount
    def get(self, key):
        return self.data.get(key, 0)
    def report(self):
        return dict(self.data)
def handle_error(error, context=None, log_path="audit.jsonl"):
    """Centralized error handler: logs error, context, and writes to audit log."""
    msg = f"ERROR: {error}"
    if context:
        msg += f" | Context: {context}"
    print(msg)
    audit_log_write(log_path, {"error": str(error), "context": str(context)})
class EventManager:
    def __init__(self):
        self._hooks = {}

    def register(self, event, func):
        self._hooks.setdefault(event, []).append(func)

    def trigger(self, event, *args, **kwargs):
        for func in self._hooks.get(event, []):
            func(*args, **kwargs)
import argparse

def parse_cli_args(arg_definitions: list, description: str = "") -> argparse.Namespace:
    """Generic CLI argument parser. Accepts argument definitions and description."""
    parser = argparse.ArgumentParser(description=description)
    for arg in arg_definitions:
        parser.add_argument(*arg["flags"], **arg["kwargs"])
    return parser.parse_args()
def validate_and_build_config(raw: dict, defaults: dict = None) -> dict:
    """Generic config validation and builder. Accepts raw config and optional defaults."""
    config = dict(defaults or {})
    config.update(raw)
    # Enforce safe defaults
    if "dangerous_option" in config:
        raise ValueError("Unsafe config option detected: dangerous_option")
    # Add more validation logic as needed
    return config
def audit_log_write(audit_path: str, record: dict) -> None:
    """Write a record to a centralized audit log (JSONL file)."""
    safe_makedirs(os.path.dirname(audit_path))
    rec = dict(record)
    rec.setdefault("ts", utc_iso())
    line = json.dumps(rec, ensure_ascii=False) + "\n"
    with open(audit_path, "a", encoding="utf-8") as f:
        f.write(line)
def run_id_utc() -> str:
    """Return a unique run ID based on UTC time."""
    return time.strftime("%Y%m%d-%H%M%SZ", time.gmtime())

def transfer_file(src: str, dest_dir: str, dry_run: bool, action: str, move_action="move", copy_action="copy") -> str:
    """Move or copy a file to a destination directory, handling collisions."""
    safe_makedirs(dest_dir)
    base = os.path.basename(src)
    target = os.path.join(dest_dir, base)
    if os.path.exists(target):
        name, ext = os.path.splitext(base)
        target = os.path.join(dest_dir, f"{name}_{int(time.time())}{ext}")
    if dry_run:
        return target
    if action == move_action:
        shutil.move(src, target)
    elif action == copy_action:
        shutil.copy2(src, target)
    else:
        raise ValueError(f"Invalid transfer action: {action}")
    return target
# engine.py
"""
Reusable engine core for launching config-driven products.
Extracted from TurboSort, designed for extensibility.
"""
import os
import sys
import json
import logging
import time
from typing import Any, Dict, Optional

def utc_iso() -> str:
    """Return current UTC time in ISO format."""
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

def manifest_init(per_run_path: str, latest_manifest_path: str) -> None:
    """Initialize manifest files."""
    safe_makedirs(os.path.dirname(latest_manifest_path))
    with open(per_run_path, "w", encoding="utf-8"):
        pass
    with open(latest_manifest_path, "w", encoding="utf-8"):
        pass

def manifest_write(manifest_paths: tuple, record: dict) -> None:
    """Write a record to manifest files."""
    per_run_path, latest_path = manifest_paths
    safe_makedirs(os.path.dirname(per_run_path))
    rec = dict(record)
    rec.setdefault("ts", utc_iso())
    line = json.dumps(rec, ensure_ascii=False) + "\n"
    with open(per_run_path, "a", encoding="utf-8") as f:
        f.write(line)
    with open(latest_path, "a", encoding="utf-8") as f:
        f.write(line)

def load_config(path: str) -> Dict[str, Any]:
    """Load a JSON config file from the given path."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def normalize_path(p: str) -> str:
    """Expand user and environment variables and normalize a path."""
    return os.path.normpath(os.path.expandvars(os.path.expanduser(p)))

def setup_logging(log_path: str, log_level: str = "INFO", name: Optional[str] = None) -> None:
    """Set up logging to file and stdout."""
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    level = getattr(logging, (log_level or "INFO").upper(), logging.INFO)
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_path, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )
    if name:
        logging.info(f"{name} started")
    else:
        logging.info("Engine started")


def safe_makedirs(p: str) -> None:
    """Create directories if they do not exist."""
    if not p:
        return
    os.makedirs(p, exist_ok=True)

def apply_placeholders(path_template: str, placeholders: Dict[str, str]) -> str:
    """Replace placeholders in a string with values from a dict."""
    out = path_template
    for k, v in placeholders.items():
        out = out.replace("{" + k + "}", v)
    return out

def is_within(child: str, parent: str) -> bool:
    """Check if child path is within parent path."""
    try:
        child_abs = os.path.abspath(child)
        parent_abs = os.path.abspath(parent)
        common = os.path.commonpath([child_abs, parent_abs])
        return common == parent_abs
    except Exception:
        return False

def scan_files_multi(input_roots, skip_dirnames_func, recursive=True, logger=None) -> list:
    """Scan files in multiple input roots, skipping directories as needed."""
    all_files = []
    for input_root in input_roots:
        if not input_root or not os.path.isdir(input_root):
            if logger:
                logger.warning(f"Input root does not exist or is not a directory: {input_root}")
            continue
        skip_dirnames = skip_dirnames_func(input_root)
        for root, dirs, files in os.walk(input_root):
            if skip_dirnames:
                dirs[:] = [d for d in dirs if d not in skip_dirnames]
            for name in files:
                all_files.append((input_root, os.path.join(root, name)))
            if not recursive:
                break
    return all_files
