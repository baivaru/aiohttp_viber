import aiohttp
from viber.utils.common import ViberCommon


class FourSquare:
    def __init__(self):
        self.endpoint = f"https://api.foursquare.com/v2/venues/search?" \
                        f"client_id={ViberCommon.foursquare_client_id}&" \
                        f"client_secret={ViberCommon.foursquare_client_secret}"

    def sear_near_by(self, query, location):
        pass