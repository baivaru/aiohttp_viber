from tinydb import TinyDB, Query
from viber.utils.common import ViberCommon


class ViberDB:
    def __init__(self):
        self.db = TinyDB(ViberCommon.db)
        self.bills_collection = self.db.table("bills")
        self.resolutions_collection = self.db.table("resolutions")
        self.approvals_collection = self.db.table("approvals")
        self.emergency_debates_collection = self.db.table("emergency")
        self.others_collection = self.db.table("others")
        self.gazette_collection = self.db.table("gazette")
        self.songs_collection = self.db.table("songs")
        self.users_collection = self.db.table("users")
        self.query = Query()


