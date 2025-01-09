import importlib
import os
from pathlib import Path

from myeditor.plugin_base import PluginBase


def load_plugins(plugin_dir):
    plugins = []
    for filename in os.listdir(plugin_dir):
        if filename.endswith(".py"):
            module_name = filename[:-3]  # Remove .py extension
            module = importlib.import_module(f"plugins.{module_name}")
            for name, obj in vars(module).items():
                if isinstance(obj, type) and issubclass(obj, PluginBase) and obj != PluginBase:
                    try:
                        plugins.append(obj())
                    except Exception as e:
                        print(f"Error loading plugin {filename}: {e}")
    return plugins


if __name__ == "__main__":
    plugin_directory = Path(__file__).parent / "plugins"
    plugins = load_plugins(plugin_directory)
    text = "Hello, world!"
    for plugin in plugins:
        formatted_text = plugin.format_text(text)
        print(f"Plugin: {type(plugin).__name__}, Formatted Text: {formatted_text}")