#!/usr/bin/env python3
# DESCRIPTION {{{1
"""
Get Window Title

Outputs the title of the window that is currently in focus.

Usage:
    get-window-title
"""

# IMPORTS {{{1
from docopt import docopt
from inform import Error, display, panic
from shlib import Run, set_prefs
set_prefs(use_inform=True)
import json

# GLOBALS {{{1
get_tree_cmd = 'swaymsg --raw --type get_tree'
__version__ = '0.0'
__released__ = '2023-11-18'

# UTILITIES {{{1
def flatten(tree, nodes):
    nodes.append(tree)
    for node in tree.get('nodes', []):
        flatten(node, nodes)

def names_of_focused(windows):
    return [window.get('name') for window in windows if window.get('focused')]

# MAIN {{{1
def main():
    cmdline = docopt(__doc__, version=__version__)

    try:
        swaymsg = Run(get_tree_cmd, 'sOEW')
        tree = json.loads(swaymsg.stdout)
        windows = []
        flatten(tree, windows)
        focused = names_of_focused(windows)
        combined = '\n'.join(focused)
        if len(focused) > 1:
            panic('more than one focused window found.', culprit=combined)
        display(combined)
    except Error as e:
        e.terminate()
    except KeyboardInterrupt:
        pass
