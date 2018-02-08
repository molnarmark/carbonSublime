# 🖥 Sublime Text 3 Integration for [Carbon](https://carbon.now.sh).

## Installation
Place the `carbonSublime.py` in your User directory.
It will be available via Package Control if people find it useful.

## Usage
Add this to your Sublime keymap file:
`
    {"keys": ["f3"], "command": "carbon_sublime"},
`
Then go into your file, select a region, and press the bound key.

## Configuration
You can find the configuration file in the folder where you placed the plugin.
It defaults to:
`
{
  "background-color": "rgba(12,108,189,1)",
  "color-scheme": "yeti"
}
`
