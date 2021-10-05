
class Controller():
    
    def __init__(self, keystroke_recorder, mouse_recorder):
        self.keystrokes = keystroke_recorder

    def start_recording(self):
        self.keystrokes.start()

    def stop_recording(self):
        self.keystrokes.stop()