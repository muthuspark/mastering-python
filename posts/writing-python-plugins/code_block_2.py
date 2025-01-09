class PluginBase:
    def format_text(self, text):
        raise NotImplementedError("Plugins must implement format_text")