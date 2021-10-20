# Based on : https://stackoverflow.com/questions/35700140/pygtk-run-gtk-main-loop-in-a-seperate-thread

import threading
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Wnck', '3.0') 
from gi.repository import GObject, Wnck

import time #TODO: Delete Later
from .Recorder import Recorder

class WindowHistoryRecorder(Recorder):
    def creation(self,this_screen: Wnck.Screen, opened_window: Wnck.Window):
        if self.rec:
            try:
                print('hello')
                self.wh_dict[opened_window] = {opened_window.get_name()}
                # app: self.Wnck.Application = opened_window.get_application()
                # app_name = app.get_name()
                # print('app name -> ' + app_name)
                # print('window name -> ' + opened_window.get_name())
            except AttributeError:
                pass

    def destruction(self,this_screen: Wnck.Screen, closed_window: Wnck.Window):
        if self.rec:
            try:
                print('goodbye')
                print(closed_window.get_name())
                # app: self.Wnck.Application = closed_window.get_application()
                # app_name = app.get_name()
                # print('app name -> ' + app_name)
                # print('window name -> ' + closed_window.get_name())
            except AttributeError:
                pass

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
        self.wh_dict = {}
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

        # TODO: put everything in the database
        for key in self.wh_dict:
            print(key)

        self.dict = {}