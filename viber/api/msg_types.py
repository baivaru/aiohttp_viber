from viber.utils.common import ViberCommon


class ViberMessageTypes:
    def __init__(self):
        self.sender_name = ViberCommon.viber_name,
        self.sender_avatar = ViberCommon.viber_avatar

    async def text_message(self, receiver, text):
        msg_obj = {
            "receiver": receiver,
            "min_api_version": 1,
            "sender": {
                "name": self.sender_name,
                "avatar": self.sender_avatar
            },
            "tracking_data": "tracking data",
            "type": "text",
            "text": text
        }
        return msg_obj
