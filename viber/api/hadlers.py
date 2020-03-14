from viber.utils.common import ViberCommon
from viber.api.request_sender import ViberApiRequestSender
from viber.api.msg_types import ViberMessageTypes


class ViberHandlers:
    def __init__(self):
        self.auth_token = ViberCommon.viber_auth_token
        self.sender_name = ViberCommon.viber_name
        self.sender_avatar = ViberCommon.viber_avatar

    async def on_event(self, data):
        event = data['event']
        if event == 'subscribed':
            await ViberHandlers().on_subscription(data)
        elif event == 'unsubscribed':
            pass
        elif event == 'conversation_started':
            pass
        elif event == 'message':
            await ViberHandlers().on_message(data)

    async def on_subscription(self, data):
        receiver = data["user"]["id"]
        receiver_name = data["user"]["name"]
        message = await ViberMessageTypes().text_message(receiver, f"Hello {receiver_name}!!")
        payload = await ViberHandlers()._prepare_payload(message=message,
                                                         sender_name=self.sender_name,
                                                         sender_avatar=self.sender_avatar,
                                                         sender=None,
                                                         receiver=receiver,
                                                         chat_id=None)
        await ViberApiRequestSender().post('send_message', payload)

    async def on_message(self, data):
        message_type = data['message']['type']
        receiver = data["sender"]["id"]
        if message_type == 'text':
            message_text = data['message']['text']
            message = await ViberMessageTypes().text_message(receiver, f"received {message_text}")
            payload = await ViberHandlers()._prepare_payload(message=message,
                                                             sender_name=self.sender_name,
                                                             sender_avatar=self.sender_avatar,
                                                             sender=None,
                                                             receiver=receiver,
                                                             chat_id=None)
            await ViberApiRequestSender().post('send_message', payload)

    async def _prepare_payload(self, message, sender_name, sender_avatar, sender=None, receiver=None, chat_id=None):
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

        return await ViberHandlers()._remove_empty_fields(payload)

    async def _remove_empty_fields(self, message):
        return {k: v for k, v in message.items() if v is not None}
