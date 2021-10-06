# import gi
# gi.require_version('Gtk', '3.0')
# gi.require_version('Wnck', '3.0')
# from gi.repository import Gtk, Wnck




# def flip(screen, previous_window):
#     try:
#         screen.force_update()
#         print(screen.get_active_window().get_name())
#         # print(
#         #     previous_window.get_name(), "||",
#         #     screen.get_active_window().get_name()
#         # )
#         # or run any action
#     except AttributeError:
#         pass

# # from
# # gi.require_version("Wnck", "3.0")


# if __name__ == '__main__':
#     wnck_scr = Wnck.Screen.get_default()
#     # wnck_scr.force_update()
#     # wnck_scr.connect("active-window-changed", flip)
#     # Gtk.main()

# import Xlib
# import Xlib.display
# import time

# run = True
# while run:
#     try:
#         time.sleep(1)

#         display = Xlib.display.Display()
#         root = display.screen().root
#         windowID = root.get_full_property(display.intern_atom('_NET_ACTIVE_WINDOW'), Xlib.X.AnyPropertyType).value[0]
#         window = display.create_resource_object('window', windowID)

#         print(window.get_wm_name())
#         print(window.get_full_property(display.intern_atom('_NET_WM_PID'), Xlib.X.AnyPropertyType).value[0])
#         print(window.get_full_property(display.intern_atom('_NET_WM_NAME'), Xlib.X.AnyPropertyType).value[0])
#         print(window.get_full_property(display.intern_atom('_NET_WM_VISIBLE_NAME'), Xlib.X.AnyPropertyType))
#         print(window.get_wm_class())
#     except KeyboardInterrupt:
#         run = False

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Wnck', '3.0')
from gi.repository import Gtk, Wnck
import time

if __name__ == '__main__':
  screen = Wnck.Screen.get_default()
  screen.force_update()
  while True:
    while Gtk.events_pending():
      Gtk.main_iteration()
    time.sleep(0.5)
    print(screen.get_active_window().get_name())