

# 🖥 Carbon Sublime

## Getting Started
Carbon Sublime (or Carbon Enhanced via Package Control) is a Sublime Text 3 Plugin for [Carbon](https://carbon.now.sh).

### Installation
Install Carbon Enhanced via Package Control.


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
	"background-color": "rgba(12,108,189,1)",
	"color-scheme": "seti",
	"drop-shadow": "true",
	"line-numbers": "true",
	"window-controls": "true"
}
```
