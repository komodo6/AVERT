from pynput import keyboard, mouse
from pynput.keyboard import Key
from threading import Thread
from .CaptureScreenshot import CaptureScreenshot

class ScreenshotRecorder():
    def __init__(self):
        self.mouse_listener = mouse.Listener(on_click=self.on_click)
        self.keyboard_listener = keyboard.Listener(on_release=self.on_release)
        self.running = False
        self.mouse_listener.start()
        self.keyboard_listener.start()

    def on_release(self, key):
        if self.running:
            print('{0} released'.format(key))
            if key == Key.esc or key == Key.enter or key == Key.tab:
                cs = CaptureScreenshot()
                cs.start()
                cs.join()

    def on_click(self, x, y, button, pressed):
        if self.running:
            cs = CaptureScreenshot()
            cs.start()
            cs.join()

    def stop(self):
        self.running = False

    def start(self):
        self.running = True
