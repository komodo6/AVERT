from db import db


class KeystrokeDAO:
    def __init__(self) -> None:
        self.db = db

    def create(self, keystroke):
        if keystroke is not None:
            self.db.keystrokes.insert(keystroke.toJSON())
        else:
            raise Exception("Cannot Insert, Keystroke is empty")
    
    def read(self, keystroke_id):
        if keystroke_id is None:
            self.db.keystrokes.find({})
        else:
            return self.db.keystrokes.find({"id": keystroke_id})

    def update(self, keystroke):
        if keystroke is not None:
            self.db.keystrokes.save(keystroke.toJSON())
        else:
            raise Exception("Cannot update, keystroke is empty")

    def delete(self, keystroke):
        if keystroke is not None:
            self.db.keystrokes.remove(keystroke.toJSON())
        else:
            raise Exception("Cannot Delete, Keystroke is empty")

    
    
ks = KeystrokeDAO()
ks.fetchAll()

# if __name__ == '__main__':
 