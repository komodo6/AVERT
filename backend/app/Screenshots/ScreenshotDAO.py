from app import db


class ScreemshotDAO:
    def __init__(self) -> None:
        self.db = db.Screenshots

    def create(self, screenshot):
        if screenshot is not None:
            self.db.insert(screenshot.toJSON())
        else:
            raise Exception("Cannot Insert, Mouse Action is empty")

    def read_id(self, screen_shot_id=None):
        # print(self.db.find({}))
        return self.db.find({"id": screen_shot_id}, {'_id': False})

    def read_all(self):
        return self.db.find({}, {'_id': False})

    def update(self, screenshot):
        if screenshot is not None:
            self.db.save(screenshot.toJSON())
        else:
            raise Exception("Cannot update, Mouse Action is empty")

    def update_tag(self, id, tags):
        if id is not None:
            self.db.update({'id': id}, {
                "$set": {
                    'tags': tags
                }
            }, upsert=False, multi=False)
        else:
            raise Exception("Cannot update, Mouse Action is empty")

    def delete(self, screenshot):
        if screenshot is not None:
            self.db.remove({'id': screenshot})
        else:
            raise Exception("Cannot Delete, Mouse Action is empty")
