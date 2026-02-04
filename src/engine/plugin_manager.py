# Plugin loader for JohnEngine
import importlib
import os
import sys

class PluginManager:
    def __init__(self, plugin_dir):
        self.plugin_dir = plugin_dir
        self.plugins = {}

    def discover_plugins(self):
        sys.path.insert(0, self.plugin_dir)
        for fname in os.listdir(self.plugin_dir):
            if fname.endswith(".py") and not fname.startswith("__"):
                mod_name = fname[:-3]
                try:
                    mod = importlib.import_module(mod_name)
                    self.plugins[mod_name] = mod
                except Exception as e:
                    print(f"Failed to load plugin {mod_name}: {e}")
        sys.path.pop(0)

    def get_plugin(self, name):
        return self.plugins.get(name)

    def all_plugins(self):
        return self.plugins.values()

    def run_plugin(self, name, *args, **kwargs):
        from engine.sandbox import run_in_sandbox
        plugin = self.get_plugin(name)
        if plugin and hasattr(plugin, "run"):
            try:
                return run_in_sandbox(plugin.run, *args, **kwargs)
            except Exception as e:
                from engine import handle_error
                handle_error(e, context=f"Plugin {name}")
        return None
