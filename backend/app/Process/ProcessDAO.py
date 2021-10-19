from app import db

class ProcessDAO:
    def __init__(self) -> None:
        self.db = db.Processes

    def create(self, process):
        if process is not None:
            self.update(process)
        else:
            raise Exception("Cannot Insert, Mouse Action is empty")

    def read(self, process_id=None):
        # print(self.db.find({}))
        if process_id is None:
            return self.db.find({}, {'_id': False})
        else:
            return self.db.find({"id": process_id}, {'_id': False})

    def update(self, process):
        if process is not None:
            query = {'proc_pid': process.toJSON()['proc_pid']}
            update = { '$set': process.toJSON() }
            self.db.update_one(query ,update, upsert=True)
            
        else:
            raise Exception("Cannot update, Mouse Action is empty")

    def delete(self, process):
        if process is not None:
            self.db.remove(process.toJSON())
        else:
            raise Exception("Cannot Delete, Mouse Action is empty")
