# Based on : https://stackoverflow.com/questions/35700140/pygtk-run-gtk-main-loop-in-a-seperate-thread

import threading
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Wnck', '3.0') 
from gi.repository import GObject

import time #TODO: Delete Later

class WindowHistoryRecorder():


    def window_switch_handler(self,screen, window):
        if self.rec:
            try:
                cur_win=screen.get_active_window().get_application().get_name()
                print(cur_win)
            except AttributeError:
                pass

    def run_gui_thread(self):
        from gi.repository import GObject
        # GObject.threads_init()
        from gi.repository import Gtk
        self.gui_ready.set()
        Gtk.main()

    def start_rec(self):
        # self.rec = True
        self.scr =  self.Wnck.Screen.get_default()
        self.scr.connect("active-window-changed", self.window_switch_handler)
        print('In start_rec',self.rec)
        while True:
            while self.Gtk.events_pending():
                self.Gtk.main_iteration()
        # print('Its YeahBoi')
        # self.GLib.idle_add(self.Gtk.main_quit)

    def __init__(self):
        self.rec = False
        self.gui_ready = threading.Event()
        self.gui_thread = threading.Thread(target=self.run_gui_thread)
        self.gui_thread.start()
        self.gui_ready.wait()
        from gi.repository import GObject, Gtk, GLib, Wnck
        self.Wnck = Wnck
        self.Gtk = Gtk
        self.GLib = GLib
        self.worker = threading.Thread(target=self.start_rec)
        print('starting work...')
        self.worker.start()
    
    def start(self):
        self.rec = True

    def stop(self):
        self.rec = False
        # self.gui_ready = None
        # self.gui_thread = None
        # self.Wnck = None
        # self.Gtk = None
        # self.GLib = None
        # self.worker = None