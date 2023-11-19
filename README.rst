Avendesora-Sway Utilities
=========================

:Authors: Ken Kundert
:Version: 0.0
:Released: 2023-11-08


Introduction
------------

These utility programs are needed to allow `Avendesora 
<https://avendesora.readthedocs.io`_ to work the `Sway <https://swaywm.org>`_ 
window manager.  *Avendesora* was originally designed for the *X11* window 
system, but *Sway* uses the new *Wayland* window system.  *Avendesora* relied on 
specific utilities so that it could interact with *X11*.  There are similar 
utilities for *Wayland* but they are not backward compatible with the *X11* 
utilities.

*Avendesora* version 1.26 and later defines a collection of generic tasks.  To 
adapt it to the different *Wayland* window managers, you need to provide scripts 
that perform the needed tasks.  This package provides the scripts needed to 
interface *Avendesora* with the *Sway* window manager.  To configure 
*Avendesora* for *Sway*, install the utilities using::

    pip install

Then set the following settings in the *Avendesora* ``config`` file::

    get_active_window_title_executable = '/home/ken/bin/get-window-title'
    copy_to_clipboard_executable = '/home/ken/bin/copy-to-clipboard'
    clear_clipboard_executable = '/home/ken/bin/clear-clipboard'
    send_mouse_click_executable = '/home/ken/bin/send-mouse-click'
    send_keystrokes_executable = '/home/ken/bin/send-keystrokes'

The paths given should be adjusted to match the full path to where you installed 
your utilities.

These utilities require that  *ydotool* and *wl-clipboard* be installed with 
your Linux package manager.  *ydotool* is very needy.  It has a daemon, 
*ydotoold* that must be run as root.  It should be configured as a systemd 
service, which is enabled and started.  Currently *ydotool* has trouble finding 
its daemon, so you need to set an environment variable to tell it how to find 
it.  This variable must be set before *Sway* is started.  To do that, create 
``~/.config/sway/environment`` and be sure it includes the following line::

    export YDOTOOL_SOCKET=/tmp/.ydotool_socket

