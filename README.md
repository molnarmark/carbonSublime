

# 🖥 Carbon Sublime

## Getting Started
Carbon Sublime (or Carbon via Package Control) is a Sublime Text 3 Plugin for [Carbon](https://carbon.now.sh).

### Installation
Install Carbon via Package Control.


### Usage
Add this to your Sublime keymap file:
```json
{"keys": ["f3"], "command": "carbon_sublime"},
```
Then go into your file, select a region, and press the bound key.

### Configuration
You can find the configuration file in the User folder. (`Preferences -> Browse Packages -> User`)\
It defaults to:
```json
{
  "background-color": "rgba(12, 108, 189, 1)",
  "theme": "seti",
  "drop-shadow": "true",
  "window-controls": "true",
  "width-adjustment": "true",
  "padding-vertical": "48px",
  "padding-horizontal": "32px",
  "line-numbers": "true",
  "language_mapping": {}
}
```
