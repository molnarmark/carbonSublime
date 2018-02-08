import sublime
import sublime_plugin
import webbrowser
from urllib.parse import urlparse

settingsFile = "carbonSublime.sublime-settings"
settings = None

class CarbonSublimeCommand(sublime_plugin.TextCommand):
  def run(self, view):
    self.generate_carbon_link(view)

  def generate_carbon_link(self, view):
    global settings
    body = self.view.substr(sublime.Region(self.view.sel()[0].a, self.view.sel()[0].b)).strip().replace("\n", "%0A").replace("\t", "%09")

    baseUrl = "https://carbon.now.sh/"
    queryString = "?bg={}&t={}&ds=true&wc=true&wa=true&pv=48px&ph=32px&ln=true&code={}".format(settings.get("background-color"), settings.get("color-scheme"), body)
    uri = urlparse(baseUrl + queryString).geturl()
    webbrowser.open(uri)

def plugin_loaded():
  global settings
  settings = sublime.load_settings(settingsFile)
  if not settings.has("color-scheme"):
    settings.set("color-scheme", "seti")
    settings.set("background-color", "rgba(12,108,189,1)")

  sublime.save_settings(settingsFile)