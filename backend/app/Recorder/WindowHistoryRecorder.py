# import subprocess
# cmd = ['xrandr']
# cmd2 = ['grep', '*']
# p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
# p2 = subprocess.Popen(cmd2, stdin=p.stdout, stdout=subprocess.PIPE)
# p.stdout.close()
# resolution_string, junk = p2.communicate()
# resolution = resolution_string.split()[0]
# width, height = resolution.split(b'x')

# print(width.decode())
# print(height.decode())


# import gi
# gi.require_version('Gtk','3.0')
# gi.require_version('Wnck','3.0')

# from gi.repository import Gtk, Wnck
# import time

# Gtk.init([])  # necessary only if not using a Gtk.main() loop
# screen = Wnck.Screen.get_default()
# screen.force_update()  # recommended per Wnck documentation

# # loop all windows
# for window in screen.get_windows():
#     print( window.get_name()) # Works
#     # print(window.get_application().get_name()) # Works
#     # print(window.is_below()) # Work
#     # print(window.is_above()) # Works
#     # print(window.is_fullscreen()) # Works
#     # print(window.is_maximized()) # works
#     print(window.get_window_type())
#     print()

    
#     # ... do whatever you want with this window

# # clean up Wnck (saves resources, check documentation)
# window = None
# screen = None
# Wnck.shutdown()

import gi
gi.require_version('Gtk','3.0')
gi.require_version('Wnck','3.0')
from gi.repository import Gtk, Wnck
import time

# while Gtk.events_pending():
#     Gtk.main_iteration()

global scr, rec_flag 


# def recording

def init():
    global src 
    global rec_flag
    # Gtk.init([rec_flag])
    scr =  Wnck.Screen.get_default()
    scr.connect("active-window-changed", window_switch_handler)
  

def start():
    global rec_flag
    rec_flag = True
    
def stop():
    global rec_flag
    rec_flag = False    

def window_switch_handler(screen, window):
    global rec_flag
    if rec_flag:
        try:
            cur_win=screen.get_active_window().get_application().get_name()
            print(cur_win)
        except AttributeError:
            pass
  
init()
start()
Gtk.main()
# Gtk.main_quit()


