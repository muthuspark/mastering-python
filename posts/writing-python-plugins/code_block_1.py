from myeditor.plugin_base import PluginBase

class ItalicPlugin(PluginBase):
    def format_text(self, text):
        return f"*{text}*"