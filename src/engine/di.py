# Simple dependency injection container
class DIContainer:
    def __init__(self):
        self._services = {}
    def register(self, name, service):
        self._services[name] = service
    def get(self, name):
        return self._services.get(name)
    def inject(self, func):
        def wrapper(*args, **kwargs):
            for k, v in self._services.items():
                if k not in kwargs:
                    kwargs[k] = v
            return func(*args, **kwargs)
        return wrapper
