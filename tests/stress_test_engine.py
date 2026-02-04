
import threading
import time
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from engine.plugin_manager import PluginManager
from engine.task_manager import TaskManager
from engine import Metrics, handle_error

PLUGIN_DIR = "src/plugins"
NUM_PLUGINS = 10
NUM_TASKS = 100

# Create dummy plugins for stress test
def create_dummy_plugins():
    import os
    for i in range(NUM_PLUGINS):
        with open(f"{PLUGIN_DIR}/dummy_plugin_{i}.py", "w") as f:
            f.write(f"def run():\n    print('Dummy plugin {i} running')\n")

create_dummy_plugins()

# Stress test plugin loading
pm = PluginManager(PLUGIN_DIR)
pm.discover_plugins()
print(f"Loaded {len(pm.plugins)} plugins.")

# Stress test task manager
metrics = Metrics()
tm = TaskManager()

def dummy_task(i):
    try:
        time.sleep(0.01)
        metrics.inc("tasks_completed")
    except Exception as e:
        handle_error(e, context=f"Task {i}")

threads = []
for i in range(NUM_TASKS):
    t = threading.Thread(target=dummy_task, args=(i,))
    t.start()
    threads.append(t)
for t in threads:
    t.join()

print(f"Completed {metrics.get('tasks_completed')} tasks.")

# Stress test plugin execution
for name, plugin in pm.plugins.items():
    plugin.run()

print("Stress test complete.")
