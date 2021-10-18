from app import db


class ScreemshotDAO:
    def __init__(self) -> None:
        self.db = db.Screenshots

    def create(self, screenshot):
        if screenshot is not None:
            self.db.insert(screenshot.toJSON())
        else:
            raise Exception("Cannot Insert, Mouse Action is empty")

    def read(self, screen_shot_id=None):
        # print(self.db.find({}))
        if screen_shot_id is None:
            return self.db.find({}, {'_id': False})
        else:
            return self.db.find({"image_id": screen_shot_id}, {'_id': False})

    def update(self, screenshot):
        if screenshot is not None:
            self.db.save(screenshot.toJSON())
        else:
            raise Exception("Cannot update, Mouse Action is empty")

    def delete(self, screenshot):
        if screenshot is not None:
            self.db.remove(screenshot.toJSON())
        else:
            raise Exception("Cannot Delete, Mouse Action is empty")
