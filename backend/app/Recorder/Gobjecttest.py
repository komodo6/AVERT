import threading
import gi




gi.require_version('Gtk', '3.0')
gi.require_version('Wnck', '3.0') 
from gi.repository import GObject
gui_ready = threading.Event()
def run_gui_thread():
    from gi.repository import GObject
    # GObject.threads_init()
    from gi.repository import Gtk
    gui_ready.set()
    Gtk.main()
gui_thread = threading.Thread(target=run_gui_thread)
gui_thread.start()
gui_ready.wait()
from gi.repository import GObject, Gtk, GLib, Wnck
import time

def window_switch_handler(screen, window):
        try:
            cur_win=screen.get_active_window().get_application().get_name()
            print(cur_win)
        except AttributeError:
            pass

def start():
    global rec
    rec = True
    scr =  Wnck.Screen.get_default()
    scr.connect("active-window-changed", window_switch_handler)
    while rec:
        while Gtk.events_pending():
            Gtk.main_iteration()
    GLib.idle_add(Gtk.main_quit)

def stop():
    global rec
    rec = False

worker = threading.Thread(target=start)
print('starting work...')
worker.start()
time.sleep(10)
stop()
