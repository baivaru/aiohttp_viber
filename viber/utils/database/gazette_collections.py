from viber.utils.database import ViberDB


class GazetteCollection:
    def __init__(self):
        self.collection = ViberDB().gazette_collection
        self.query = ViberDB().query

    async def gazette_updates_from_scheduler(self, title, volume, link, date):
        if not self.collection.search(self.query.link == link):
            self.collection.insert(
                {
                    'title': title,
                    'volume': volume,
                    'link': link,
                    'date': date
                }
            )

    async def gazette_return_collection(self):
        documents = self.collection.all()
        data = []
        for document in documents:
            _data = {
                'title': document['title'],
                'volume': document['volume'],
                'link': document['link'],
                'date': document['date']
            }
            data.append(_data)

        return data
