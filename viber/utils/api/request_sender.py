import hashlib
import hmac

import aiohttp
import logging
from viber.utils.common import ViberCommon


class ViberApiRequestSender:
    def __init__(self):
        self.headers = {
            'User-Agent': "ViberBot-Python/0.0.1"
        }
        self.web_hook = 'https://chatapi.viber.com/pa/set_webhook'
        self.send_message = 'https://chatapi.viber.com/pa/send_message'
        self.broadcast_message = 'https://chatapi.viber.com/pa/broadcast_message'
        self.account_info = 'https://chatapi.viber.com/pa/get_account_info'
        self.user_details = 'https://chatapi.viber.com/pa/get_user_details'
        self.get_online = 'https://chatapi.viber.com/pa/get_online'
        self.auth_token = ViberCommon.viber_auth_token

    async def post(self, uri, payload):
        headers = self.headers
        endpoint = getattr(self, uri)
        async with aiohttp.ClientSession() as session:
            async with session.post(url=endpoint, json=payload, headers=headers) as resp:
                logging.info(await resp.text())
                return await resp.json()

    async def validate_signature(self, received_signature, data):
        calculated_signature = hmac.new(
            bytes(self.auth_token.encode('ascii')),
            msg=str(data).encode(),
            digestmod=hashlib.sha256).hexdigest()
        return calculated_signature == received_signature
