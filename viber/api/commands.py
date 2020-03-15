from viber.api.msg_types import ViberMessageTypes
from viber.api.request_sender import ViberApiRequestSender
from viber.helpers.scrapers import Scrapers
from viber.utils.common import ViberCommon


class ViberCommands:
    def __init__(self):
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
            bills = await Scrapers().collect_bills()
            message = await ViberMessageTypes().rich_media(receiver, bills)
            payload = await ViberCommands().prepare_payload(message=message,
                                                            sender_name=self.sender_name,
                                                            sender_avatar=self.sender_avatar,
                                                            sender=None,
                                                            receiver=receiver,
                                                            chat_id=None)
            await ViberApiRequestSender().post('send_message', payload)
        elif command == "resolutions":
            resolutions = await Scrapers().collect_resolutions()
            message = await ViberMessageTypes().rich_media(receiver, resolutions)
            payload = await ViberCommands().prepare_payload(message=message,
                                                            sender_name=self.sender_name,
                                                            sender_avatar=self.sender_avatar,
                                                            sender=None,
                                                            receiver=receiver,
                                                            chat_id=None)
            await ViberApiRequestSender().post('send_message', payload)
        elif command == "emergency_debates":
            emergency_debates = await Scrapers().collect_emergency_debates()
            message = await ViberMessageTypes().rich_media(receiver, emergency_debates)
            payload = await ViberCommands().prepare_payload(message=message,
                                                            sender_name=self.sender_name,
                                                            sender_avatar=self.sender_avatar,
                                                            sender=None,
                                                            receiver=receiver,
                                                            chat_id=None)
            await ViberApiRequestSender().post('send_message', payload)
        elif command == "approvals":
            approvals = await Scrapers().collect_approvals()
            message = await ViberMessageTypes().rich_media(receiver, approvals)
            payload = await ViberCommands().prepare_payload(message=message,
                                                            sender_name=self.sender_name,
                                                            sender_avatar=self.sender_avatar,
                                                            sender=None,
                                                            receiver=receiver,
                                                            chat_id=None)
            await ViberApiRequestSender().post('send_message', payload)
        elif command == "others":
            others = await Scrapers().collect_others()
            message = await ViberMessageTypes().rich_media(receiver, others)
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
