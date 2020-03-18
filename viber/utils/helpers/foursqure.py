import aiohttp
from viber.utils.common import ViberCommon


class FourSquare:
    def __init__(self):
        self.endpoint = f"https://api.foursquare.com/v2/venues/search?" \
                        f"client_id={ViberCommon.foursquare_client_id}&" \
                        f"client_secret={ViberCommon.foursquare_client_secret}&radius=100&limit=6&v=20200319"

    async def sear_near_by(self, location):
        endpoint = f"{self.endpoint}&ll={location['lat']},{location['lon']}"
        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as resp:
                data = await resp.json()
                venues = []

                for venue in data['response']['venues']:
                    _venue = {
                        'name': venue['name'],
                        'lat': venue['location']['lat'],
                        'lon': venue['location']['lng'],
                        'address': venue['location']['address'] if 'address' in venue['location'] else None,
                        'street': venue['location']['crossStreet'] if 'crossStreet' in venue['location'] else None,
                    }
                    try:
                        _venue['contact'] = venue['contact']['phone'] if 'phone' in venue['contact'] else None
                    except KeyError:
                        _venue['contact'] = None

                    venues.append(_venue)
        return venues
