from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os
import subprocess

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    #Flip windows between vertical/horizontal
    Key([mod, "mod1"], "j", lazy.layout.flip_down(),
        desc="Flip window down"),
    Key([mod, "mod1"], "k", lazy.layout.flip_up(),
        desc="Flip window up"),
    Key([mod, "mod1"], "h", lazy.layout.flip_left(),
        desc="Flip window left"),
    Key([mod, "mod1"], "l", lazy.layout.flip_right(),
        desc="Flip window right"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key(
        [mod, "shift"], "f",
        lazy.window.toggle_floating(),
        desc='toggle floating'),
    Key(
        [mod, "mod1"], "Return", lazy.window.toggle_fullscreen(),
        desc="toggle fullscreen"),
    Key(["mod1"], "space", lazy.spawn("rofi -show drun"), desc="rofi launcher"),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"),
        desc="mute audio"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -3000"), desc="decrese volume"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +3000"), desc="increase volume"),
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui"), desc="take screenshot"),
    Key([], "XF86TouchpadToggle", lazy.spawn("/home/kurosaki/.config/qtile/toggle-touchpad.sh"), desc="toggle touchpad"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
        Key([mod, "control"], "q", lazy.shutdown(),
            desc="Exit Qtile"),
    ])

layout_theme = {
    "border_focus": "a6d189",
    "border_normal": "737994",
    "border_width": 3
}

layouts = [
    layout.Bsp(
        fair=False,
        margin=4,
        margin_on_single=5,
        **layout_theme),
    #layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    layout.Floating(**layout_theme)
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='monospace',
    fontsize=12,
    padding=2,
    background='#303446'
)
extension_defaults = widget_defaults.copy()
Sep = widget.Sep(
    foreground='#babbf1',
    linewidth=2,
    padding=4,
    size_percent=60,
)

screens = [
    Screen(
        #wallpaper config
        wallpaper="~/.themes/kotoseduce.jpg",
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.GroupBox(
                    inactive='737994',
                    hide_unused=True,
                    rounded=True,
                    this_current_screen_border='a6d189',
                    this_screen_border='babbf1',
                ),
                widget.CurrentScreen(
                    active_color='a6d189',
                    inactive_color='e78284',
                ),
                Sep,
                widget.Prompt(
                    prompt='Launch: ',
                ),
                widget.TaskList(
                    border='a6d189',
                    unfocused_border='737994',
                    borderwidth=3,
                     txt_floating='🗗 ',
                    txt_maximized='🗖 ',
                    txt_minimized='🗕 ',
                ),
                widget.Systray(),
                Sep,
                widget.CurrentLayoutIcon(
                    scale=0.6,
                ),
                Sep,
                widget.CapsNumLockIndicator(
                    update_interval=0.1
                ),
                Sep,
                widget.CPU(
                    format='CPU {load_percent}%',
                ),
                Sep,
                widget.Memory(
                    format='MEM {MemUsed: .2f}{mm}/{MemTotal: .0f}{mm}',
                    measure_mem='G',
                ),
                Sep,
                widget.Backlight(
                    backlight_name='intel_backlight',
                    format='BL {percent:2.0%}',
                    step=1,
                ),
                Sep,
                widget.Volume(
                    update_interval=0.05,
                    step=1,
                    fmt='VOL {}',
                ),
                Sep,
                widget.Battery(
                    format='BAT {char} {percent:2.0%} {watt:.2f}W',
                    low_percentage=0.15,
                    low_foreground='e78284',
                    update_interval=15,
                ),
                Sep,
                widget.Clock(
                    format='%Y/%m/%d %a %H:%M:%S',
                ),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='pqiv'),
    Match(wm_class='zoom'),
    Match(wm_class='megasync'),
    Match(wm_class='xdman'),
    Match(wm_class='jdownloader'),
    ], **layout_theme)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things lik e steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

#autostart hook
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
