import time
from pynput import mouse
from src.models.MouseActions import MouseActions

class MouseActionRecord:

    '''
    When using the non - blocking version below, the current thread will
    continue executing.This might be necessary when integrating
    with other GUI frameworks that incorporate a main-loop, but 
    when run from a script, this will cause the program to terminate immediately.
    '''

    def initiate(self):
        print("made init")
        self.running = False
        self.listener = mouse.Listener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll)
        self.listener.start()

    def start(self):
        self.running = True

    def stop(self):
        print('stop')
        self.running = False

    def makeClass(self):
        pass

    def on_move(self,x, y):
        if self.running:
            print("on_move")
            print(x, ',', y)

    def on_click(self,x, y, button, pressed):
        if not self.running:
            print("on_click")
            print(x, ',', y)
            print('pressed: ', pressed)
            print('button: ', button)

    def on_scroll(self,x, y, dx, dy):
        if not self.running:
            print('on_scroll')
            print(x, ',', y)
            print('dy', dy)

    def make_mouse_action(self):
        # IP
        # MAC
        # Time Stamp
        pass


mouse_action_recorder = MouseActionRecord()
mouse_action_recorder.initiate()

while True:
    print('Beginning----------------------------------------------------------------------------------------\n\n\n\n\n\n\n\n\n')
    time.sleep(4)

    mouse_action_recorder.start()

    print("Before the sleep")
    time.sleep(4)
    print("after the sleep")

    mouse_action_recorder.stop()




