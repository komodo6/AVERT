from .Recorder import Recorder
from app.MouseAction.MouseActionsDAO import MouseActionsDAO
from pynput import mouse
from app.models.MouseAction import MouseAction
from app.models.Annotation import Annotation

# from services.ActiveWindow import ActiveWindow
# import gi
# gi.require_version('Gtk', '3.0')
# gi.require_version('Wnck', '3.0')
# from gi.repository import Gtk, Wnck

class MouseActionRecorder(Recorder):
    '''
    When using the non - blocking version below, the current thread will
    continue executing.This might be necessary when integrating
    with other GUI frameworks that incorporate a main-loop, but 
    when run from a script, this will cause the program to terminate immediately.
    '''

    def __init__(self) -> None:
        super().__init__()
        self.ip = super().get_ip()
        self.mac = super().get_mac()
        self.mouse_action_collection = MouseActionsDAO()
        self.running = False
        self.listener = mouse.Listener(
            on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll)
        self.listener.start()

        # move this to where you start recording
        # self.aw = ActiveWindow()
        # self.aw.start()

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def on_move(self, x, y):
        if self.running:
            a = Annotation(self.ip, None)
            self.mouse_action_collection.create(MouseAction(super().get_timestamp(
            ), self.ip, self.mac, a.toJSON(), type='on_move', coord_x=x, coord_y=y, active_window=None))

    def on_click(self, x, y, button, pressed):
        if self.running:
            a = Annotation(self.ip, None)
            self.mouse_action_collection.create(MouseAction(super().get_timestamp(
            ), self.ip, self.mac, a.toJSON(), type='on_click', coord_x=x, coord_y=y, pressed=pressed, button=button.name, active_window=None))

    def on_scroll(self, x, y, dx, dy):
        if self.running:
            a = Annotation(self.ip, None)
            self.mouse_action_collection.create(MouseAction(super().get_timestamp(
            ), self.ip, self.mac, a.toJSON(), type='on_click', coord_x=x, coord_y=y, scroll=dy, active_window=None))

    
