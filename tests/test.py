"""Tests functions and classes in carbonSublime.py.
"""

import sys
import unittest
from unittest import mock
import webbrowser

import sublime

carbonSublime = sys.modules['carbonSublime.carbonSublime']


class TestViewMixin:
    def setUp(self):
        self.view = sublime.active_window().new_file()

    def tearDown(self):
        if self.view:
            self.view.set_scratch(True)
            window = self.view.window()
            window.focus_view(self.view)
            window.run_command("close_file")


class TestHelperFunctions(TestViewMixin, unittest.TestCase):
    def test_convert_tabs_using_tab_size_tab_2(self):
        original = "\t\tprint('Hello')"
        expected = "    print('Hello')"

        self.view.settings().set("tab_size", 2)
        result = carbonSublime.convert_tabs_using_tab_size(self.view, original)
        self.assertEquals(result, expected)

    def test_convert_tabs_using_tab_size_tab_4(self):
        original = "\t\tprint('Hello')"
        expected = "        print('Hello')"

        self.view.settings().set("tab_size", 4)
        result = carbonSublime.convert_tabs_using_tab_size(self.view, original)
        self.assertEquals(result, expected)


class TestCarbonSublimeCommand(TestViewMixin, unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.command = carbonSublime.CarbonSublimeCommand(self.view)

    def test_normalize_code_no_indent(self):
        original = "def hello(name):  \n    print('Hello, ' + name))  "
        expected = "def hello(name):\n    print('Hello, ' + name))"
        self.add_and_select_text(original)

        code = self.command.normalize_code()
        self.assertEquals(code, expected)

    def test_normalize_code_with_indent(self):
        self.view.settings().set("tab_size", 4)
        original = "\tdef hello(name):  \n\t\tprint('Hello, ' + name))  "
        expected = "def hello(name):\n    print('Hello, ' + name))"
        self.add_and_select_text(original)

        code = self.command.normalize_code()
        self.assertEquals(code, expected)

    def test_normalize_code_no_selection(self):
        self.view.settings().set("tab_size", 4)
        original = "\tdef hello(name):  \n\t\tprint('Hello, ' + name))  \n"
        expected = "    def hello(name):\n        print('Hello, ' + name))"
        self.add_text(original)

        code = self.command.normalize_code()
        self.assertEquals(code, expected)

    @mock.patch.object(webbrowser, 'open')
    def test_generate_carbon_link(self, open):
        self.assertFalse(open.called)

        code = "print('Hello')"
        self.command.generate_carbon_link(code)
        self.assertTrue(open.called)

    def add_and_select_text(self, text):
        self.add_text(text)
        selection = self.view.sel()
        selection.clear()
        selection.add(sublime.Region(0, self.view.size()))

    def add_text(self, text):
        # Uses `insert_snippet` instead of `insert`
        # as `insert` doesn't honor indents.
        self.view.run_command("insert_snippet", {"contents": text})
