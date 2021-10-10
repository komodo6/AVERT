from app import db


class KeystrokeDAO:
    def __init__(self) -> None:
        self.db = db.Keystrokes

    def create(self, keystroke):
        if keystroke is not None:
            self.db.insert(keystroke.toJSON())
        else:
            raise Exception("Cannot Insert, Keystroke is empty")

    def read(self, keystroke_id=None):
        if keystroke_id is None:
            print(self.db)
            return self.db.find({}, {'_id': False})
        else:
            return self.db.find({"id": keystroke_id}, {'_id': False})

    def update(self, keystroke):
        if keystroke is not None:
            self.db.save(keystroke.toJSON())
        else:
            raise Exception("Cannot update, keystroke is empty")

    def delete(self, keystroke):
        if keystroke is not None:
            self.db.remove(keystroke.toJSON())
        else:
            raise Exception("Cannot Delete, Keystroke is empty")