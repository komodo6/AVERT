from app import db
import gridfs
import os
fs = gridfs.GridFS(db)
import datetime


current_dir = os.path.dirname(os.path.abspath(__file__))
class PacketCaptureDAO():

    def __init__(self):
        self.nd = db.NetworkData
        self.np = db.NetworkPackets

    def get_count(self):
        print(self.np.count())
        return self.np.count()

    def createPCAP(self, networkdata):
        pcapPath = os.path.join(current_dir, f"../pcaps/{networkdata.pcapfile}")
        try:
            obj = networkdata.__dict__
            self.nd.insert(obj)
            
            fs.put(open(pcapPath, "rb"), filename=networkdata.pcapfile)
        except Exception as e :
            print(e)
        finally:
            os.remove(pcapPath)
    

    def createPacket(self, packdata):
        print(packdata)
        return self.np.insert(packdata, check_keys=False)

    def getAllPCAPS(self):
        return list(self.nd.find())

    def getPacketFile(self, filename):
        data = fs.find_one({"filename": filename})
        pcapPath = os.path.join(current_dir, f"../pcaps/temps/{filename}")
        with open(pcapPath, "wb") as f:
            f.write(data.read())
        
        return pcapPath
    
    def getPackets(self, filename):
        return list(self.np.find({"pcapfileID": filename}))
    
    def getPacketsBYID(self, id):
        return list(self.np.find({"_id": id}))

    