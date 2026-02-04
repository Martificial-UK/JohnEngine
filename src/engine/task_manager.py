import threading
import time

class TaskManager:
    def __init__(self):
        self.tasks = {}

    def run_task(self, name, func, *args, **kwargs):
        t = threading.Thread(target=func, args=args, kwargs=kwargs)
        t.start()
        self.tasks[name] = t
        return t

    def wait_for(self, name):
        t = self.tasks.get(name)
        if t:
            t.join()

    def all_tasks(self):
        return self.tasks
