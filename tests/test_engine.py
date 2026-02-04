
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from engine import engine

class TestEngineCore(unittest.TestCase):
    def test_load_config(self):
        # Create a sample config file
        sample_path = "test_config.json"
        sample_data = {"foo": "bar"}
        with open(sample_path, "w", encoding="utf-8") as f:
            import json
            json.dump(sample_data, f)
        loaded = engine.load_config(sample_path)
        self.assertEqual(loaded["foo"], "bar")

    def test_normalize_path(self):
        self.assertTrue(isinstance(engine.normalize_path("~/"), str))

    def test_run_id_utc(self):
        rid = engine.run_id_utc()
        self.assertTrue(rid.startswith("20"))

    def test_audit_log_write(self):
        path = "test_audit.jsonl"
        engine.audit_log_write(path, {"event": "test"})
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        self.assertIn("event", lines[-1])

if __name__ == "__main__":
    unittest.main()
