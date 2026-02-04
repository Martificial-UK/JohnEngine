class HealthCheck:
    def __init__(self):
        self.checks = []
    def register(self, func):
        self.checks.append(func)
    def run(self):
        results = {}
        for func in self.checks:
            try:
                results[func.__name__] = func()
            except Exception as e:
                results[func.__name__] = f"ERROR: {e}"
        return results
