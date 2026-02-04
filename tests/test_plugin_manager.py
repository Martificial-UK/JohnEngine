import unittest
import os
from engine.plugin_manager import PluginManager

class TestPluginManager(unittest.TestCase):
    def test_discover_and_run_plugin(self):
        plugin_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src/plugins"))
        pm = PluginManager(plugin_dir)
        pm.discover_plugins()
        plugin = pm.get_plugin("example_plugin")
        self.assertIsNotNone(plugin)
        # Should print output from plugin
        plugin.run()

if __name__ == "__main__":
    unittest.main()
