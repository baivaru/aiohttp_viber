from viber.utils.common import ViberCommon
from viber.utils.api.request_sender import ViberApiRequestSender
from viber.utils.api.msg_types import ViberMessageTypes
from viber.utils.api.commands import ViberCommands
from viber.utils.api.tracking_data import ViberTrackingDataAttendant
from viber.utils.database.users import ViberUsers


class ViberHandlers:
    def __init__(self):
        self.auth_token = ViberCommon.viber_auth_token
        self.sender_name = ViberCommon.viber_name
        self.sender_avatar = ViberCommon.viber_avatar
    @staticmethod
    async def on_event(data):
        global msg_trail
        event = data['event']
        if event == 'subscribed':
            await ViberHandlers().on_subscription(data)
        elif event == 'unsubscribed':
            await ViberHandlers().on_unsubscribed(data)
        elif event == 'message':
            await ViberHandlers().on_message(data)

    async def on_subscription(self, data):
        receiver = data["user"]["id"]
        receiver_name = data["user"]["name"]
        message = await ViberMessageTypes().text_message(receiver, f"Hello {receiver_name}!!", None, None)
        payload = await ViberCommands().prepare_payload(message=message,
                                                        sender_name=self.sender_name,
                                                        sender_avatar=self.sender_avatar,
                                                        sender=None,
                                                        receiver=receiver,
                                                        chat_id=None)
        await ViberApiRequestSender().post('send_message', payload)

        # also add the user to DB
        await ViberUsers().add_user(receiver, receiver_name)

    @staticmethod
    async def on_unsubscribed(data):
        receiver = data["user_id"]
        await ViberUsers().remove_user(receiver)

    @staticmethod
    async def on_message(data):
        message_type = data['message']['type']
        if 'tracking_data' in data['message']:
            tracking_data = data['message']['tracking_data']
            await ViberTrackingDataAttendant().attend(tracking_data, data)
        else:
            if message_type == 'text':
                await ViberCommands().text_validator(data)
