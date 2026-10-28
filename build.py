# Generates themes/flexoki-vscode.json from the colors of the sglza.flexoki VS Code theme.
import json
import pathlib

bg = "#100f0f"
bg2 = "#1c1b1a"
ui = "#282726"
tx = "#cecdc3"
tx2 = "#878580"
tx3 = "#575653"
red = "#d14d41"
orange = "#da702c"
yellow = "#d0a215"
green = "#879a39"
cyan = "#3aa99f"
blue = "#4385be"
purple = "#8b7ec8"
magenta = "#ce5d97"
bright_red = "#e35535"
punctuation = "#d3d8e160"


def style(color, font_style=None, font_weight=None):
    return {
        "color": color,
        "background_color": None,
        "font_style": font_style,
        "font_weight": font_weight,
    }


def tinted(color, alpha):
    return color + alpha


status = {}
for name, color in {
    "conflict": purple,
    "created": green,
    "deleted": red,
    "error": orange,
    "hidden": tx3,
    "hint": tx2,
    "ignored": tx2,
    "info": blue,
    "modified": orange,
    "predictive": tx3,
    "renamed": blue,
    "success": green,
    "unreachable": tx2,
    "warning": yellow,
}.items():
    status[name] = color
    status[f"{name}.background"] = tinted(color, "1a")
    status[f"{name}.border"] = tinted(color, "4d")

ui_style = {
    "background.appearance": "opaque",
    "border": ui,
    "border.variant": bg2,
    "border.focused": tinted(blue, "99"),
    "border.selected": tinted(blue, "66"),
    "border.transparent": "#00000000",
    "border.disabled": bg2,
    "elevated_surface.background": bg2,
    "surface.background": bg,
    "background": bg,
    "element.background": ui,
    "element.hover": bg2,
    "element.active": ui,
    "element.selected": ui,
    "element.disabled": bg2,
    "drop_target.background": "#383b3d80",
    "ghost_element.background": "#00000000",
    "ghost_element.hover": bg2,
    "ghost_element.active": ui,
    "ghost_element.selected": ui,
    "ghost_element.disabled": "#00000000",
    "text": tx,
    "text.muted": tx2,
    "text.placeholder": "#a6a6a6",
    "text.disabled": tx3,
    "text.accent": blue,
    "icon": tx,
    "icon.muted": tx2,
    "icon.disabled": tx3,
    "icon.placeholder": tx2,
    "icon.accent": blue,
    "status_bar.background": ui,
    "title_bar.background": bg,
    "title_bar.inactive_background": bg,
    "toolbar.background": bg,
    "tab_bar.background": bg,
    "tab.inactive_background": bg,
    "tab.active_background": bg,
    "search.match_background": "#ea5c0055",
    "search.active_match_background": "#515c6aff",
    "panel.background": bg,
    "panel.focused_border": None,
    "pane.focused_border": None,
    "pane_group.border": "#444444",
    "scrollbar.thumb.background": "#79797966",
    "scrollbar.thumb.hover_background": "#646464b3",
    "scrollbar.thumb.active_background": "#bfbfbf66",
    "scrollbar.thumb.border": "#00000000",
    "scrollbar.track.background": "#00000000",
    "scrollbar.track.border": "#00000000",
    "minimap.thumb.background": "#79797933",
    "minimap.thumb.hover_background": "#64646466",
    "minimap.thumb.active_background": "#bfbfbf33",
    "editor.foreground": tx,
    "editor.background": bg,
    "editor.gutter.background": bg,
    "editor.subheader.background": bg2,
    "editor.active_line.background": "#ffffff0a",
    "editor.highlighted_line.background": "#ffffff0b",
    "editor.line_number": "#858585",
    "editor.active_line_number": "#c6c6c6",
    "editor.hover_line_number": "#c6c6c6",
    "editor.invisible": "#e3e4e229",
    "editor.wrap_guide": "#5a5a5a40",
    "editor.active_wrap_guide": "#5a5a5a80",
    "editor.indent_guide": "#404040",
    "editor.indent_guide_active": "#707070",
    "editor.document_highlight.read_background": "#57575780",
    "editor.document_highlight.write_background": "#00497280",
    "editor.document_highlight.bracket_background": "#0064001a",
    "terminal.background": bg,
    "terminal.foreground": "#cccccc",
    "terminal.bright_foreground": "#e5e5e5",
    "terminal.dim_foreground": "#666666",
    "terminal.ansi.background": bg,
    "terminal.ansi.black": "#000000",
    "terminal.ansi.bright_black": "#666666",
    "terminal.ansi.dim_black": "#000000",
    "terminal.ansi.red": "#cd3131",
    "terminal.ansi.bright_red": "#f14c4c",
    "terminal.ansi.dim_red": "#8f2222",
    "terminal.ansi.green": "#0dbc79",
    "terminal.ansi.bright_green": "#23d18b",
    "terminal.ansi.dim_green": "#098354",
    "terminal.ansi.yellow": "#e5e510",
    "terminal.ansi.bright_yellow": "#f5f543",
    "terminal.ansi.dim_yellow": "#a0a00b",
    "terminal.ansi.blue": "#2472c8",
    "terminal.ansi.bright_blue": "#3b8eea",
    "terminal.ansi.dim_blue": "#194f8c",
    "terminal.ansi.magenta": "#bc3fbc",
    "terminal.ansi.bright_magenta": "#d670d6",
    "terminal.ansi.dim_magenta": "#832c83",
    "terminal.ansi.cyan": "#11a8cd",
    "terminal.ansi.bright_cyan": "#29b8db",
    "terminal.ansi.dim_cyan": "#0c758f",
    "terminal.ansi.white": "#e5e5e5",
    "terminal.ansi.bright_white": "#e5e5e5",
    "terminal.ansi.dim_white": "#a0a0a0",
    "link_text.hover": blue,
    "version_control.added": green,
    "version_control.modified": blue,
    "version_control.deleted": "#94151b",
    "version_control.word_added": "#9bb95533",
    "version_control.word_deleted": "#ff000033",
    "version_control.conflict_marker.ours": "#27403b",
    "version_control.conflict_marker.theirs": "#28384b",
    **status,
    "players": [
        {"cursor": "#aeafad", "background": "#aeafad", "selection": "#264f78"},
        {"cursor": blue, "background": blue, "selection": tinted(blue, "3d")},
        {"cursor": orange, "background": orange, "selection": tinted(orange, "3d")},
        {"cursor": purple, "background": purple, "selection": tinted(purple, "3d")},
        {"cursor": cyan, "background": cyan, "selection": tinted(cyan, "3d")},
        {"cursor": red, "background": red, "selection": tinted(red, "3d")},
        {"cursor": yellow, "background": yellow, "selection": tinted(yellow, "3d")},
        {"cursor": green, "background": green, "selection": tinted(green, "3d")},
    ],
    "accents": [yellow, magenta, blue, purple, cyan, red],
}

syntax = {
    "attribute": style(yellow),
    "attribute.builtin": style(magenta),
    "boolean": style(bright_red),
    "comment": style(tx2, "italic"),
    "comment.doc": style(tx2, "italic"),
    "constant": style(red),
    "constant.builtin": style(bright_red),
    "constructor": style(purple),
    "diff.minus": style(bright_red),
    "diff.plus": style("#3cec85"),
    "embedded": style(tx),
    "emphasis": style(orange, "italic"),
    "emphasis.strong": style(red, None, 700),
    "enum": style(purple),
    "function": style(blue),
    "function.decorator": style(magenta),
    "function.kwargs": style(magenta),
    "hint": style(tx2),
    "keyword": style(yellow),
    "keyword.definition": style(cyan),
    "keyword.function": style(cyan),
    "keyword.storage": style(cyan),
    "label": style(blue),
    "link_text": style(blue),
    "link_uri": style(blue),
    "namespace": style(blue),
    "module": style(blue),
    "number": style(orange),
    "operator": style(yellow),
    "predictive": style(tx3, "italic"),
    "preproc": style(yellow),
    "primary": style(tx),
    "property": style(orange),
    "punctuation": style(punctuation),
    "punctuation.bracket": style(punctuation),
    "punctuation.delimiter": style(punctuation),
    "punctuation.list_marker": style(blue),
    "punctuation.markup": style(yellow),
    "punctuation.special": style(bright_red),
    "selector": style(blue),
    "selector.pseudo": style(magenta),
    "string": style(green),
    "string.doc": style("#3cec8560"),
    "string.escape": style(bright_red),
    "string.regex": style(green),
    "string.special": style(bright_red),
    "string.special.symbol": style(green),
    "tag": style(blue),
    "text.literal": style(purple),
    "title": style(yellow),
    "type": style(purple),
    "variable": style(red),
    "variable.builtin": style(cyan),
    "variable.parameter": style(magenta),
    "variable.special": style(orange),
    "variant": style(purple),
}

theme = {
    "$schema": "https://zed.dev/schema/themes/v0.2.0.json",
    "name": "Flexoki VSCode",
    "author": "vaqxai",
    "themes": [
        {
            "name": "Flexoki VSCode",
            "appearance": "dark",
            "style": {**ui_style, "syntax": syntax},
        }
    ],
}

output = pathlib.Path(__file__).parent / "themes" / "flexoki-vscode.json"
output.write_text(json.dumps(theme, indent=2) + "\n")
