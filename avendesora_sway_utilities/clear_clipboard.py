#!/usr/bin/env python3
# DESCRIPTION {{{1
"""
Clear Clipboard

Usage:
    clear-clipboard
"""

# IMPORTS {{{1
from docopt import docopt
from inform import Error
from shlib import Run, Start, set_prefs
set_prefs(use_inform=True)

# GLOBALS {{{1
clear_cmd = ['wl-copy', '--primary', '--clear']
__version__ = '0.0'
__released__ = '2023-11-18'


# MAIN {{{1
def main():
    docopt(__doc__, version=__version__)

    try:
        Run(clear_cmd, modes='sOEW')
    except Error as e:
        e.terminate()
    except KeyboardInterrupt:
        pass
