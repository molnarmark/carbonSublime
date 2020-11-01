![](https://raw.githubusercontent.com/molnarmark/carbonSublime/master/assets/header.png)

<p align="center">
  <img src="https://img.shields.io/github/v/release/molnarmark/carbonsublime"/>
  <img src="https://img.shields.io/badge/-Sublime%20Text%203-black?style=flat-rounded&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAMAAAAolt3jAAAAAXNSR0IB2cksfwAAAAlwSFlzAAALEwAACxMBAJqcGAAAALFQTFRFAAAA/681/6w2/6s2/6s2/6w2/6s2/6s2/6s2/6s2/642/6w2/6s2/6s2/6s2/6s2/6s2/6s2/6s2/6s2/6s2/603/ao2/6s2/6w2/641/6s2/6s2/6w2/qw2/6s2/6s2/6s2/qs29qU1/ao2/6w2/6s2/6s28KEz35Yv4pgw96Y1/6s29qU05psx4Zgw6p0y/6s2/6s2/6s26J0y/6s2/6s2/6s2/6s2/q02/6s2/6w2Gw5i1gAAADt0Uk5TAAEwd74LM73s/wJHod385+/+5a5cB/JqGQHbhjEugtcXWtP/H4HJ9P///8z////78siDHdygWh8CWRR3ufuBAAAAc0lEQVR4nGNggAJGJmYWGJuVjZmdg5MTzObi5uHl4wQBMJefEwoEwFwwU1BIWEQUwRUTl5BkQHA5OaWkZcBcWTl5qAjUHgVFJWUEV0VVTV1DUwvK1RYEyejo6ukjGWVgaGQM5fKZmJqZW0ANEuKxtII5HgC7swjoiG1GPAAAAABJRU5ErkJggg=="/>
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
