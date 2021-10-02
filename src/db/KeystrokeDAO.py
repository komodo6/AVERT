import db

class KeystrokeDAO:
    def __init__(self) -> None:
        self.db = db['Keycloak']

    def fetchAll(self):
        print(db)
        
    
    