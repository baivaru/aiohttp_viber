import random
import aiohttp
from viber.utils.common import ViberCommon


class PixbayVideos:
    def __init__(self):
        self.end_point = f'https://pixabay.com/api/videos/?key={ViberCommon.pixbay_key}&q=diving&per_page=50'

    async def get_random_video(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.end_point) as resp:
                data = await resp.json()
                random_hit = random.randrange(50)
                video_hit = data['hits'][random_hit]
                video_url = video_hit['videos']['medium']['url']
                video_size = video_hit['videos']['medium']['size']
                thumb_id = video_hit['picture_id']
                duration = video_hit['duration']
                video_data = {
                    'url': video_url,
                    'size': video_size,
                    'thumb': f'https://i.vimeocdn.com/video/{thumb_id}_960x540.jpg',
                    'duration': duration
                }

                return video_data
