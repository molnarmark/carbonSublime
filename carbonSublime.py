import sublime
import sublime_plugin
import webbrowser, os
from urllib.parse import urlencode

settings_file = 'carbonSublime.sublime-settings'
settings = None

# Carbon language mapping
LANGUAGE_MAPPING = {
    'Auto': 'auto',
    'Apache': 'text/apache',
    'Shell-Unix-Generic': 'application/x-sh',
    'Plain text': 'text',
    'C': 'text/x-csrc',
    'C++': 'text/x-c++src',
    'C#': 'text/x-csharp',
    'Clojure': 'clojure',
    'Cobol': 'cobol',
    'CoffeeScript': 'coffeescript',
    'Crystal': 'crystal',
    'CSS': 'css',
    'D': 'd',
    'Dart': 'dart',
    'Diff': 'text/x-diff',
    'Django': 'django',
    'Docker': 'dockerfile',
    'Elixir': 'elixir',
    'Elm': 'elm',
    'Erlang': 'erlang',
    'Fortran': 'fortran',
    'F#': 'mllike',
    'OCaml': 'mllike',
    'GraphQL': 'graphql',
    'Go': 'go',
    'Groovy': 'groovy',
    'Handlebars': 'handlebars',
    'Haskell': 'haskell',
    'Haxe': 'haxe',
    'HTML': 'htmlmixed',
    'Java': 'text/x-java',
    'JavaScript': 'javascript',
    'JavaScript (Babel)': 'javascript',
    'JavaScriptNext': 'javascript',
    'JSON': 'application/json',
    'JSON (Sublime)': 'application/json',
    'JSX': 'jsx',
    'Julia': 'julia',
    'Kotlin': 'text/x-kotlin',
    'Lisp': 'commonlisp',
    'Lua': 'lua',
    'Markdown': 'markdown',
    'Mathematica': 'mathematica',
    'MySQL': 'text/x-mysql',
    'NGINX': 'nginx',
    'Nim': 'nimrod',
    'Objective-C': 'text/x-objectivec',
    'Pascal': 'pascal',
    'Perl': 'perl',
    'PHP': 'text/x-php',
    'PowerShell': 'powershell',
    'Python': 'python',
    'R': 'r',
    'Ruby': 'ruby',
    'Rust': 'rust',
    'Sass': 'sass',
    'Scala': 'text/x-scala',
    'Smalltalk': 'smalltalk',
    'SQL': 'sql',
    'Swift': 'swift',
    'TCL': 'tcl',
    'TypeScript': 'application/typescript',
    'VB.NET': 'vb',
    'Verilog': 'verilog',
    'VHDL': 'vhdl',
    'Vue': 'vue',
    'XML': 'xml',
    'YAML': 'yaml'
}

#
# START - util functions
#

# Converts tabs into spaces
def convert_tabs_using_tab_size(view, string):
  tab_size = view.settings().get("tab_size")
  
  if tab_size:
    return string.replace("\t", " " * tab_size)

  return string.replace("\t", " ")

# Get how much whitespace is in the current region from the gutter compared to the begin of the region
def get_whitespace_from_line_begin(view, region) :
  n_space = len(view.substr(view.line(region.begin()))) - len(view.substr(view.line(region.begin())).lstrip())
  return " " * n_space

#
# END - util functions
#

class CarbonSublimeCommand(sublime_plugin.TextCommand):

    def run(self, edit, **kwargs):
        code = self.normalize_code()
        self.generate_carbon_link(code)

    def normalize_code(self):
        view = self.view
        whitespace = ""
        body = ""
        code = ""

        if view.sel()[0].begin() != view.sel()[0].end():
            # consider the only selected text
            # 
            # get whitespace of the current selection
            whitespace = convert_tabs_using_tab_size(view, get_whitespace_from_line_begin(view, view.sel()[0]))
            body = view.substr(view.sel()[0])
        else:
            # no text selected, so consider the whole view
            body = view.substr(sublime.Region(0, view.size()))

        body = convert_tabs_using_tab_size(view, body.strip())

        # Put only about 3400 characters on the URL string. More than that won't work (in that case use https://carbon.now.sh directly).
        body = body[0:3400]
        
        # create the final code that will be sent to the carbon.sh website
        for line in body.splitlines():
            # remove whitespace from the right
            line = line.rstrip()
            # index_start start to 0 the first time for the first line
            index_start = len(whitespace) if code else 0
            # start considering the line at index_start in order to normalize the text (deleting useless whitespaces)
            code += line[index_start:] + "\n"

        return code

    def generate_carbon_link(self, code):
        global settings
        view = self.view

        # get current view syntax
        syntax = os.path.splitext(os.path.basename(view.settings().get("syntax")))[0]
        if syntax in LANGUAGE_MAPPING:
            # set language from the mapping
            language = LANGUAGE_MAPPING[syntax]
        else:
            # otherwise set 'auto': Carbon will try to understand which language is used.
            language = 'auto'

        base_url = 'https://carbon.now.sh/?'
        
        query = {
            'bg'  : settings.get('background-color'),
            't'   : settings.get('theme'),
            'l'   : language,
            'ds'  : settings.get('drop-shadow'),
            'wc'  : settings.get('window-controls'),
            'wa'  : settings.get('width-adjustment'),
            'pv'  : settings.get('padding-vertical'),
            'ph'  : settings.get('padding-horizontal'),
            'ln'  : settings.get('line-numbers'),
            'code': code
        }

        webbrowser.open(base_url + urlencode(query))

def plugin_loaded():
    global settings
    settings = sublime.load_settings(settings_file)
    
    if not settings.has('window-controls'):
        settings.set('theme', 'seti')
        settings.set('background-color', 'rgba(12, 108, 189, 1)')
        settings.set('window-controls', 'true')
        settings.set('drop-shadow', 'true')
        settings.set('line-numbers', 'true')
        settings.set('width-adjustment', 'true'),
        settings.set('padding-vertical', '48px'),
        settings.set('padding-horizontal', '32px'),

    sublime.save_settings(settings_file)
