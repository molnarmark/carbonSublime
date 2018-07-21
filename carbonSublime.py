import os
from urllib.parse import urlencode
import webbrowser
import sublime
import sublime_plugin

SETTINGS_FILE = 'carbonSublime.sublime-settings'
CODE_MAX_LENGTH = 3400

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
    'YAML': 'yaml',
}


def convert_tabs_using_tab_size(view, string):
    tab_size = view.settings().get("tab_size")

    if tab_size:
        return string.replace("\t", " " * tab_size)

    return string.replace("\t", " ")


def get_whitespace_from_line_beginning(view, region):
    n_space = len(view.substr(view.line(region.begin()))) - len(
        view.substr(view.line(region.begin())).lstrip()
    )
    return " " * n_space


class CarbonSublimeCommand(sublime_plugin.TextCommand):
    def run(self, edit, **kwargs):
        code = self.normalize_code()
        self.generate_carbon_link(code)

    def normalize_code(self):
        view = self.view

        if len(view.sel()) and not view.sel()[0].empty():
            region = view.sel()[0]
            indent_size = len(get_whitespace_from_line_beginning(view, region))
        else:
            # no text selected, so consider the whole view
            region = sublime.Region(0, view.size())
            indent_size = 0

        body = view.substr(region)
        body = '\n'.join(x[indent_size:].rstrip() for x in body.splitlines())
        body = convert_tabs_using_tab_size(view, body)

        if len(body) > CODE_MAX_LENGTH:
            body = body[:CODE_MAX_LENGTH]
            view.window().status_message(
                'carbonSublime: The code was trimmed to {}.'.format(CODE_MAX_LENGTH)
            )

        return body

    def generate_carbon_link(self, code):
        view = self.view
        settings = sublime.load_settings(SETTINGS_FILE)

        # get current view syntax
        syntax = os.path.splitext(os.path.basename(view.settings().get("syntax")))[0]

        # set language from the mapping
        language_mapping = settings.get('language_mapping')
        if isinstance(language_mapping, dict) and syntax in language_mapping:
            language = language_mapping[syntax]
        elif syntax in LANGUAGE_MAPPING:
            language = LANGUAGE_MAPPING[syntax]
        else:
            language = 'auto'

        base_url = 'https://carbon.now.sh/?'

        query = {
            'bg': settings.get('background-color'),
            't': settings.get('theme'),
            'l': language,
            'ds': settings.get('drop-shadow'),
            'wc': settings.get('window-controls'),
            'wa': settings.get('width-adjustment'),
            'pv': settings.get('padding-vertical'),
            'ph': settings.get('padding-horizontal'),
            'ln': settings.get('line-numbers'),
            'code': code,
        }

        webbrowser.open(base_url + urlencode(query))
