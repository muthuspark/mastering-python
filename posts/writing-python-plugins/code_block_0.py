from myeditor.plugin_base import PluginBase

class BoldPlugin(PluginBase):
    def format_text(self, text):
        return f"**{text}**"