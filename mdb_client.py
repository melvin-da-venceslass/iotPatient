import pymongo,requests
from bson.objectid import ObjectId
import json
import time
class MDB_reader:
    def __init__(self):
        mdb_cli = pymongo.MongoClient("mongodb+srv://root:ipm721997%2A@cluster0.js7th.mongodb.net/PMON?retryWrites=true&w=majority")
        mdb_dbms = mdb_cli["PMON"]
        self.mdb_pmaster = mdb_dbms["PMASTER"]

    def get_the_patient(self,pid):
        try:
            query = {"pid":pid}
            patient = self.mdb_pmaster.find_one(query)
            del patient["_id"]
            return patient
        except:
            return False
               

    def save_the_patient(self,patient):
        try:
            if patient.operation=="modify":
                self.mdb_pmaster.update_one({"pid":patient.pid},{"$set":patient.dict()})
                return True
            elif patient.operation=="create":
                self.mdb_pmaster.insert_one(patient.dict())
                return True
            elif patient.operation=="delete":
                self.mdb_pmaster.delete_one({"pid":patient.dict()["pid"]})
                return True

        except:
            return False

