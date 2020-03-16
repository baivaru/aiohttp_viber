from viber.utils.database import ViberDB


class MajilisCollection:
    @staticmethod
    async def majilis_updates_from_scheduler(collection, name, link, status, summary):
        collection = getattr(ViberDB(), collection)
        if not collection.search(ViberDB().query.link == link):
            collection.insert(
                {
                    'name': name,
                    'link': link,
                    'status': f"މިހާރު އޮތް ހިސާބް: {status}",
                    'summary': summary
                }
            )

    @staticmethod
    async def majilis_return_collection(collection):
        collection = getattr(ViberDB(), collection)
        documents = collection.all()
        data = []
        for document in documents:
            _data = {
                'name': document['name'],
                'link': document['link'],
                'status': document['status'],
                'summary': document['summary']
            }
            data.append(_data)

        return data
