from app import db

class WindowHistoryDAO:
    def __init__(self) -> None:
        self.db = db.WindowHistories

    def create(self, wh):
        if wh is not None:
            self.db.insert(wh.toJSON())
        else:
            raise Exception("Cannot Insert, Mouse Action is empty")

    def read(self, wh_id=None):
        # print(self.db.find({}))
        if wh_id is None:
            return self.db.find({}, {'_id': False})
        else:
            return self.db.find({"id": wh_id}, {'_id': False})

    def update(self, wh):
        if wh is not None:
            self.db.save(wh.toJSON())
        else:
            raise Exception("Cannot update, Mouse Action is empty")

    def delete(self, wh):
        if wh is not None:
            self.db.remove(wh.toJSON())
        else:
            raise Exception("Cannot Delete, Mouse Action is empty")

    def get_count(self):
        print(self.db.count())
        return self.db.count()        
