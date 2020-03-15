from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

from viber.api.msg_types import ViberMessageTypes
from viber.api.request_sender import ViberApiRequestSender
from viber.utils.common import ViberCommon


class ViberCommands:
    def __init__(self):
        self.bs = BeautifulSoup
        self.req = Request
        self.url_op = urlopen
        self.auth_token = ViberCommon.viber_auth_token
        self.sender_name = ViberCommon.viber_name
        self.sender_avatar = ViberCommon.viber_avatar

    async def text_validator(self, data):
        message = data['message']['text']
        receiver = data["sender"]["id"]
        if str(message).startswith('!'):
            await ViberCommands().commands_checker(message, receiver)

    async def commands_checker(self, command, receiver):
        command = command[1:]
        if command == "bills":
            req = self.req('https://majlis.gov.mv/dv/19-parliament/parliament-works/type/1',
                           headers={'User-Agent': 'Mozilla/5.0'})
            page = self.url_op(req)
            soup = self.bs(page, 'html.parser')

            divs = soup.findAll('div', class_='col-12 my-3')

            bills = []
            for div in divs:
                data = div.findAll('a')
                for d in data[:6]:
                    req = Request(d.get('href'),
                                  headers={'User-Agent': 'Mozilla/5.0'})
                    page = urlopen(req)
                    soup = BeautifulSoup(page, 'html.parser')
                    khulaasa = soup.find('div', class_='max-600w').p
                    bill = {
                        'name': d.text,
                        'link': d.get('href'),
                        'summary': khulaasa.text.strip()
                    }
                    bills.append(bill)

            message = await ViberMessageTypes().rich_media(receiver, bills)
            payload = await ViberCommands().prepare_payload(message=message,
                                                            sender_name=self.sender_name,
                                                            sender_avatar=self.sender_avatar,
                                                            sender=None,
                                                            receiver=receiver,
                                                            chat_id=None)
            await ViberApiRequestSender().post('send_message', payload)

    async def prepare_payload(self, message, sender_name, sender_avatar, sender=None, receiver=None, chat_id=None):
        payload = message
        payload.update({
            'auth_token': self.auth_token,
            'from': sender,
            'receiver': receiver,
            'sender': {
                'name': sender_name,
                'avatar': sender_avatar
            },
            "chat_id": chat_id
        })

        return await ViberCommands()._remove_empty_fields(payload)

    async def _remove_empty_fields(self, message):
        return {k: v for k, v in message.items() if v is not None}
