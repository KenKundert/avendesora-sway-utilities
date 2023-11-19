#!/usr/bin/env python3
# DESCRIPTION {{{1
"""
Copy to Clipboard

Usage:
    copy-to-clipboard [<text>...]

If <text> is not provided, use the standard input.
"""
# This command is used by Avendesora to copy text into the Wayland clipboard.
# To simply the creation of these little scripts, Avendesora cannot specify 
# command line options.  Instead, you should hard code the desired options in 
# copy_cmd below.
# Possible options to include:
#     --primary — use primary buffer (select) rather than clipboard (ctrl-C)
#     --trim-newline — remove a trailing newline
#                      currently a no-op because text is stripped of both 
#                      leading and trailing whitespace
#     --paste-once   — only allow one copy
#                      not really needed because Avendesora automatically clears
#                      the clipboard after a minute

# IMPORTS {{{1
from docopt import docopt
from inform import Error
from shlib import Run, Start, set_prefs
set_prefs(use_inform=True)

# GLOBALS {{{1
copy_cmd = ['wl-copy', '--primary', '--foreground', '--type', 'text/plain']
    # Something funky is happening with wl-copy.  The manpage says it runs in 
    # the background by default, but when run from this script it appears to run 
    # in the foreground, which causes the script to hang until the user copies 
    # something else.  So instead, explicitly tell the wl-copy command to run in 
    # the foreground using the Start command, so this script does not wait for 
    # it to terminate.
__version__ = '0.0'
__released__ = '2023-11-18'

# MAIN {{{1
def main():
    cmdline = docopt(__doc__, version=__version__)

    try:
        if cmdline['<text>']:
            # docopt splits text into a collection of words, join them back together
            text = ' '.join(cmdline['<text>'])
        else:
            # read from stdin
            text = open(0, encoding='utf-8').read()

        # to avoid secrets being visible using ps, send the text using stdin
        Start(copy_cmd, stdin=text.strip(), modes='sOE')
    except Error as e:
        e.terminate()
    except KeyboardInterrupt:
        pass
