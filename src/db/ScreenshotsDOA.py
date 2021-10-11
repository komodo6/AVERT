from db import db
class ScreenshotsDOA:
    def __init(self) -> None:
        self.db = db.db.ScreenShots
    def create(self, screenshot):
        if screenshot is not None:
            self.db.insert(screenshot.toJSON())
        else:
            raise Exception("Cannot Insert, Screenshot is empty")

    def read(self, screenshot_id=None):
        if screenshot_id is None:
            return self.db.find({}, {'_id': False})
        else:
            return self.db.find({"id": screenshot_id}, {'_id': False})

    def update(self, screenshot):
        if screenshot is not None:
            self.db.save(screenshot.toJSON())
        else:
            raise Exception("Cannot update, Screenshot is empty")

    def delete(self, screenshot):
        if screenshot is not None:
            self.db.remove(screenshot.toJSON())
        else:
            raise Exception("Cannot Delete, Screenshot is empty")



