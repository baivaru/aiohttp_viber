from viber.utils.common import ViberCommon
from viber.utils.api.commands import ViberCommands
from viber.utils.api.msg_types import ViberMessageTypes
from viber.utils.api.request_sender import ViberApiRequestSender
from viber.utils.database.gazette_collections import GazetteCollection


class ViberTrackingDataAttendant:
    def __init__(self):
        self.sender_name = ViberCommon.viber_name
        self.sender_avatar = ViberCommon.viber_avatar

    async def attend(self, tracking_data, data):
        message = data['message']['text']
        receiver = data["sender"]["id"]
        if tracking_data == 'gazette':
            gazette = await GazetteCollection().gazette_return_collection()
            if str(message).isnumeric():
                tracked_gazette = gazette[int(message)]
                message = await ViberMessageTypes().file_message(receiver, tracked_gazette['link'], None, None)
                payload = await ViberCommands().prepare_payload(message=message,
                                                                sender_name=self.sender_name,
                                                                sender_avatar=self.sender_avatar,
                                                                sender=None,
                                                                receiver=receiver,
                                                                chat_id=None)
                await ViberApiRequestSender().post('send_message', payload)
