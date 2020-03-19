from viber.utils.database import ViberDB


class ViberUsers:
    def __init__(self):
        self.collection = ViberDB().users_collection
        self.query = ViberDB().query

    async def add_user(self, user_id, name):
        if not self.collection.search(ViberDB().query.user_id == user_id):
            self.collection.insert(
                {
                    'user_id': user_id,
                    'name': name,
                }
            )

    async def get_users(self):
        users = []
        documents = self.collection.all()
        for document in documents:
            users.append(
                {
                    'user_id': document['user_id'],
                    'name': document['name']
                }
            )

        return users

    async def remove_user(self, user_id):
        if self.collection.search(ViberDB().query.user_id == user_id):
            self.collection.remove(ViberDB().query.user_id == user_id)
