import aiohttp
from viber.utils.common import ViberCommon


class UnsplashPhotos:
    def __init__(self):
        self.end_point = \
            f"https://api.unsplash.com/photos/random/?client_id={ViberCommon.unsplash_key}&query=maldives&per_page=1"

    async def random_photo(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.end_point) as resp:
                data = await resp.json()
                photo_data = {
                    'title': data['alt_description'],
                    'username': data['user']['username'],
                    'link': data['urls']['full'],
                    'thumb': data['urls']['regular']
                }

                return photo_data
