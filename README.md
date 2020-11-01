![](https://i.imgur.com/nk0e21I.png)

## Getting Started

Carbon is a Sublime Text 3 Plugin for [Carbon](https://carbon.now.sh).

### Installation

Install _Carbon_ via Package Control.

### Usage

#### Command Palette

You can use the command `Carbon: Share Selection` from the command palette (ctrl/cmd + shift + p) to open Carbon.

#### Keymap

This package doesn't provide a default keymap. If you need to, add a keymap setting like the following to your Sublime keymap file:

```json
{ "keys": ["f3"], "command": "carbon" }
```

Then go into your file, select a region, and press the bound key.

### Configuration

You can open the configuration file via the menu:

Preferences > Package Settings > Carbon > Settings. It defaults to the **default** preset in the Carbon app:

```json
{
  "trim_indent": true,
  "default": {
    "paddingVertical": "48px",
    "paddingHorizontal": "32px",
    "backgroundImage": null,
    "backgroundImageSelection": null,
    "backgroundMode": "color",
    "backgroundColor": "rgba(72,112,126,1)",
    "dropShadow": true,
    "dropShadowOffsetY": "20px",
    "dropShadowBlurRadius": "68px",
    "theme": "seti",
    "windowTheme": "none",
    "language": "",
    "fontFamily": "Hack",
    "fontSize": "14px",
    "lineHeight": "133%",
    "windowControls": true,
    "widthAdjustment": true,
    "lineNumbers": true,
    "firstLineNumber": 1,
    "exportSize": "2x",
    "watermark": false,
    "squaredImage": false,
    "hiddenCharacters": false,
    "name": "Hello",
    "width": 680
  }
}
```

- `trim_indent`: (`bool`) If set to true, indents are trimmed when a selection is made.

### Custom Configuration

First, head over to the [Carbon](https://carbon.now.sh) app, change the configuration, then head over to the **Misc** tab, press **Export config** and replace the file contents under the **default** node.
