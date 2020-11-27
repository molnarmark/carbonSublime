![](https://raw.githubusercontent.com/molnarmark/carbonSublime/master/assets/header.png)

<p align="center">
  <img src="https://img.shields.io/github/v/release/molnarmark/carbonsublime"/>
  <img src="https://raw.githubusercontent.com/molnarmark/carbonSublime/master/assets/sublbadge.png"/>
</p>

🎨 Sublime Text 3 Plugin for **[Carbon](https://carbon.now.sh)**.

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

#### Settings

Use `Preferences: Carbon Settings` from the command palette (ctrl/cmd + shift + p)

Or you can open the configuration file via the menu:

Preferences > Package Settings > Carbon > Settings. By default, it uses the initial configuration from Carbon:

```json
{
    "trim_indent": true,
    "show_status_messages": true,
    "use_emojis_in_status_messages": true,
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

-   `trim_indent`: If set to true, lines starting with indents are trimmed. (**true** by default)
-   `show_status_messages`: If set to true, success/error messages are displayed in the status bar. (**true** by default)
-   `use_emojis_in_status_messages`: If set to true, indicator emojis are added the success/error messages in the status bar. (**true** by default)

#### Custom Configuration

![](https://raw.githubusercontent.com/molnarmark/carbonSublime/master/assets/exportconfig.png)

-   Head over to the [Carbon](https://carbon.now.sh)
-   Configure the editor to your preferred look
-   Click the **Misc** tab
-   Press **Export config**
-   Paste the downloaded configuration under the **default** property in the settings.
