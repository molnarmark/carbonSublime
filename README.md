![](https://raw.githubusercontent.com/molnarmark/carbonSublime/master/assets/header.png)

<p align="center">
  <img src="https://img.shields.io/github/v/release/molnarmark/carbonsublime"/>
  <img src="https://raw.githubusercontent.com/molnarmark/carbonSublime/master/assets/sublbadge.png"/>
</p>

🚀 Sublime Text 3 Plugin for **[Carbon](https://carbon.now.sh)**.

### Installation

Install **Carbon** via Package Control.

#### Command Palette Usage

You can use the command `Carbon: Share Selection` from the command palette (ctrl/cmd + shift + p) to open Carbon.

#### Keymap Usage

This package doesn't provide a default keymap. If you need to, add a keymap setting like the following to your Sublime keymap file:

```json
{ "keys": ["f3"], "command": "carbon" }
```

Then go into your file, select a region, and press the bound key.

#### Configuration

You can open the configuration file via the menu:

Preferences > Package Settings > Carbon > Settings. By default, it uses the initial configuration from Carbon:

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

- `trim_indent`: If set to true, lines starting with indents are trimmed.

#### Custom Configuration

![](https://raw.githubusercontent.com/molnarmark/carbonSublime/master/assets/exportconfig.png)

- Head over to the [Carbon](https://carbon.now.sh)
- Configure the editor to your preferred look
- Click the **Misc** tab
- press **Export config**
- Paste the downloaded configuration under the **default** node in the settings.
