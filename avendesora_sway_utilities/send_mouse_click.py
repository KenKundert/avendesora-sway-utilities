#!/usr/bin/env python3
# DESCRIPTION {{{1
"""
Send Mouse Click

Sends a mouse click to the active window

Usage:
    send-mouse-click
"""
# ydotool is a bit of a nightmare to use.
# 1. you need to install and run ydotoold as root
# 2. by default, ydotool cannot find the daemon's socket, so you have to set the 
#    environment variable YDOTOOL_SOCKET=/tmp/.ydotool_socket

# IMPORTS {{{1
from docopt import docopt
from inform import Error, display, panic
from shlib import Run, set_prefs
set_prefs(use_inform=True)
import json

# GLOBALS {{{1
ydotool_cmd = 'ydotool click -d 1000 0xC2'
     # left: 0xC0, right=0xC1, middle=0xC2
__version__ = '0.0'
__released__ = '2023-11-18'

# MAIN {{{1
def main():
    cmdline = docopt(__doc__, version=__version__)

    try:
        ydotool = Run(ydotool_cmd, 'sOEW')
    except Error as e:
        e.terminate(codicil=e.stdout)
    except KeyboardInterrupt:
        pass
