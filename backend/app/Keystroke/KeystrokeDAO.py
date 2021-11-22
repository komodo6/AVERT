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

    def get_size(self):
        print(self.db.dataSize())
        return self.db.dataSize()

    def update(self, keystroke):
        if keystroke is not None:
            self.db.save(keystroke.toJSON())
        else:
            raise Exception("Cannot update, keystroke is empty")

    def update_tag(self, id, tags):
        if id is not None:
            self.db.update({'id': id}, {
                "$set": {
                    'tags': tags
                }
            }, upsert=False, multi=False)
        else:
            raise Exception("Cannot update, Mouse Action is empty")

    def delete(self, keystroke):
        if keystroke is not None:
            self.db.remove(keystroke.toJSON())
        else:
            raise Exception("Cannot Delete, Keystroke is empty")
