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
        self.run()

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

    def run(self):
        # Collect events until released
        self.mouse_listener.start()
        self.keyboard_listener.start()
        self.mouse_listener.join()
        self.keyboard_listener.join()