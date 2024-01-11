from inst_options_util import bar_widgets
import os

home_dir = os.path.expanduser('~') + '/'

## Show the options to the user
print('How should the available workspace be displayed')
print('[1] Japanese style')
print('[2] Numbers style\n')
while True:
    choice = input()
    if choice == '1':
        grouplabels = ('一', '二', '三', '四', '五', '六', '七', '八', '九', '十')
        break
    elif choice == '2':
        grouplabels = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
        break

print('Where should workspaces group be on the bar')
print('[1] On the center')
print('[2] On the left')
while True:
    choice = input()
    if choice == '1':
        widgets = bar_widgets["centered"]
        break
    elif choice == '2':
        widgets = bar_widgets["on_side"]
        break

print('How should the top bar be displayed')
print('[1] Floating with a gap on top of screen')
print('[2] Fixed on top of screen')
while True:
    choice = input()
    if choice == '1':
        margin = "5, 5, 0, 5"
        fixed = False
        break
    elif choice == '2':
        margin = "0, 0, 0, 0"
        fixed = True
        break

print("Writting custom config")

# Append setting to picom.conf file
if fixed:
    with open(home_dir + '.config/picom/picom.conf', 'a') as f:
        f.write('''\
rounded-corners-exclude = [
	"QTILE_INTERNAL:32c = 1"
];
'''); f.close

# Write the costumized groups.conf file
with open(home_dir + ".config/qtile/settings/groups.py", 'w') as f:
    f.write(f'''\
from libqtile.config import Group
       
# Define available workspaces here
groups = [
    Group('1', label="{grouplabels[0]}"),
    Group('2', label="{grouplabels[1]}"),
    Group('3', label="{grouplabels[2]}"),
    Group('4', label="{grouplabels[3]}"),
    Group('5', label="{grouplabels[4]}"),
    Group('6', label="{grouplabels[5]}"),
    Group('7', label="{grouplabels[6]}"),
    Group('8', label="{grouplabels[7]}"),
    Group('9', label="{grouplabels[8]}"),
    #Group('0', label="{grouplabels[9]}"),
]

'''); f.close

# Write the costumized screenconf.py file
with open(home_dir + ".config/qtile/settings/screen.py", 'w') as f:
    f.write(f'''\
from libqtile import bar, widget
from libqtile.config import Screen
from colorpalett import colors

# Default values of the bar widgets
widget_defaults = dict(
    font="JetBrains Mono Nerd Font",
    fontsize=15,
    padding=5,
    foreground=colors["foreground"],
    background=colors["background"],
)

screens = [
    Screen(
        # Qtile bar settings
        top=bar.Bar(
            [
                {widgets}
            ],
            30,  # bar height
            margin=[{margin}],  # Draw top and bottom borders   [ top, right, bottom, left ]
        ),
    ),
]

'''); f.close
