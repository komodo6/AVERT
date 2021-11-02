from pynput import keyboard, mouse
from pynput.keyboard import Key
from threading import Thread
from .CaptureScreenshot import CaptureScreenshot

class ScreenshotRecorder():
    def __init__(self):
        self.cs = CaptureScreenshot()
        self.mouse_listener = mouse.Listener(on_click=self.on_click)
        self.keyboard_listener = keyboard.Listener(on_release=self.on_release)
        self.running = False

    def on_release(self, key):
        if self.running:
            print('{0} released'.format(key))
            if key == Key.esc or key == Key.enter or key == Key.tab:
                self.cs.start()
                self.cs.join()
        else:
            return False

    def on_click(self, x, y, button, pressed):
        if self.running:
            self.cs.start()
            self.cs.join()
        else:
            return False

    def stop(self):
        self.running = False

    def start(self):
        self.running = True
        self.run()

    def run(self):
        self.mouse_listener.start()
        self.keyboard_listener.start()