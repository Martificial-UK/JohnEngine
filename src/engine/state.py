import json

class StatePersistence:
    def __init__(self, state_path):
        self.state_path = state_path
    def save(self, state):
        with open(self.state_path, "w", encoding="utf-8") as f:
            json.dump(state, f)
    def load(self):
        try:
            with open(self.state_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
