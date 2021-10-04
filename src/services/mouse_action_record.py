import time
from pynput import mouse
from src.models.model import MouseAction
from src.models.model import MouseActionCollection


class MouseActionRecorder:

    '''
    When using the non - blocking version below, the current thread will
    continue executing.This might be necessary when integrating
    with other GUI frameworks that incorporate a main-loop, but 
    when run from a script, this will cause the program to terminate immediately.
    '''

    def initiate(self):
        self.mouse_action_collection = MouseActionCollection()
        self.running = False
        self.listener = mouse.Listener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll)
        self.listener.start()

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def on_move(self,x, y):
        if self.running:
            print(MouseAction("time","date", "ip", "mac", "annotations", type = 'on_move', coord_x=x, coord_y=y ).data_to_dict())


    def on_click(self,x, y, button, pressed):
        if self.running:
            print(MouseAction("time","date","ip","mac","annotations", type = 'on_click', coord_x=x, coord_y=y,pressed=pressed, button=button).data_to_dict())

    def on_scroll(self,x, y, dx, dy):
        if self.running:
            print(MouseAction("time", "date", "ip", "mac", "annotations", type='on_click', coord_x=x, coord_y=y, scroll=dy).data_to_dict())



mouse_action_recorder = MouseActionRecorder()
mouse_action_recorder.initiate()
mouse_action_recorder.start()
time.sleep(4)
mouse_action_recorder.stop()




