# from threading import Thread
# import gi
# gi.require_version('Gtk', '3.0')
# gi.require_version('Wnck', '3.0')
# from gi.repository import Gtk, Wnck

# class ActiveWindow(Thread):

#     def __init__(self):
#         Thread.__init__(self)
#         self.wnck_scr = Wnck.Screen.get_default()
#         self.wnck_scr.connect("active-window-changed", self.getWindow)
#         self.window = None
        

#     def run(self):
            
#             Gtk.main()

#     def getWindow(self, screen, previous_window):
#         try:
#             self.window = screen.get_active_window().get_name()
#         except AttributeError:
#             pass

        

#     def whatWindow(self):
#         return self.window

            



