# Based on : https://stackoverflow.com/questions/35700140/pygtk-run-gtk-main-loop-in-a-seperate-thread

import threading
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Wnck', '3.0') 
from gi.repository import GObject, Wnck

import time #TODO: Delete Later
from .Recorder import Recorder
import subprocess
from ..models.WindowHistory import WindowHistory
from ..WindowHistory.WindowHistoryDAO import WindowHistoryDAO

class WindowHistoryRecorder(Recorder):
    
    def get_screen_res(self):
        cmd = ['xrandr']
        cmd2 = ['grep', '*']
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        p2 = subprocess.Popen(cmd2, stdin=p.stdout, stdout=subprocess.PIPE)
        p.stdout.close()
        resolution_string, junk = p2.communicate()
        resolution = resolution_string.split()[0]
        width, height = resolution.split(b'x')    
        return [{'width':width.decode()}, {'height':height.decode()}] 

    def creation(self,this_screen: Wnck.Screen, opened_window: Wnck.Window):
        if self.rec:
            try:

                print('hello') # TODO: delete
                new_window = WindowHistory(
                    self.get_timestamp(),
                    self.get_ip(),
                    self.get_mac(),
                    None, #TODO: Add annotations
                    None, #TODO: Add tags
                    self.res,
                    None,
                    None, # TODO: Figure out how to get visibility
                    None, # TODO: Window Placement command
                    not opened_window.is_maximized(),
                    opened_window.is_maximized(),
                    opened_window.get_application().get_name(),
                    opened_window.get_window_type(),
                    opened_window.get_name(),
                    self.get_timestamp(),
                    None

                )
                self.wh_dict[opened_window.get_xid()] = new_window
            except AttributeError:
                pass

    def destruction(self,this_screen: Wnck.Screen, closed_window: Wnck.Window):
        if self.rec:
            print('goodbye')
            self.wh_dict[closed_window.get_xid()].window_destruction = self.get_timestamp()

    def run_gui_thread(self):
        from gi.repository import GObject
        # GObject.threads_init()
        from gi.repository import Gtk
        self.gui_ready.set()
        Gtk.main()

    def start_rec(self):
        self.scr =  self.Wnck.Screen.get_default()
        self.scr.connect("window-opened", self.creation)
        self.scr.connect("window-closed", self.destruction)
        while True:
            while self.Gtk.events_pending():
                self.Gtk.main_iteration()

    def __init__(self):
        self.db = WindowHistoryDAO()
        self.wh_dict = {}
        self.res = self.get_screen_res()
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
        self.worker.start()
    
    def start(self):
        self.rec = True

    def stop(self):
        self.rec = False
        print('Stopping')
        # TODO: put everything in the database
        for key in self.wh_dict:
            self.db.create(self.wh_dict[key])

        self.dict = {}