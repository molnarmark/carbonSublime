import sublime
import sublime_plugin
import webbrowser
from urllib.parse import urlencode

settings_file = 'carbonSublime.sublime-settings'
settings = None

class CarbonSublimeCommand(sublime_plugin.TextCommand):

    def run(self, view):
        self.generate_carbon_link(view)

    def generate_carbon_link(self, view):
        global settings

        body = self.view.substr(
            sublime.Region(
                self.view.sel()[0].a, self.view.sel()[0].b
            )).strip()

        base_url = 'https://carbon.now.sh/?'

        query = {
            'bg': settings.get('background-color'),
            't': settings.get('color-scheme'),
            'ds': True,
            'wc': True,
            'wa': True,
            'pv': '48px',
            'ph': '32px',
            'ln': True,
            'code': body
        }

        webbrowser.open(base_url + urlencode(query))

def plugin_loaded():
    global settings

    settings = sublime.load_settings(settings_file)

    if not settings.has('color-scheme'):
        settings.set('color-scheme', 'seti')
        settings.set('background-color', 'rgba(12,108,189,1)')

    sublime.save_settings(settings_file)
