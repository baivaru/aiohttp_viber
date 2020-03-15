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

    async def rich_media(self, receiver, data_list):
        # formulating buttons
        buttons = []
        for data in data_list[:6]:
            name = data['name']
            link = data['link']
            status = data['status']
            summary = data['summary']
            first_rows = {
                "Columns": 6,
                "Rows": 4,
                "ActionType": "open-url",
                "ActionBody": link,
                "Image": "https://upload.wikimedia.org/wikipedia/en/f/f2/Maldives_Majlis_Logo.jpeg"
            }
            buttons.append(first_rows)
            second_row = {
                "Columns": 6,
                "Rows": 1,
                "Text": f"<font color=#323232><b>{name[:250]}</b></font>",
                "ActionType": "none",
                "TextSize": "medium",
                "TextVAlign": "middle",
                "TextHAlign": "right"
            }
            buttons.append(second_row)
            third_row = {
                "Columns": 6,
                "Rows": 1,
                "Text": f"<font color=#777777 size=12>{status[:250]}</font>",
                "ActionType": "none",
                "TextSize": "medium",
                "TextVAlign": "middle",
                "TextHAlign": "right"
            }
            buttons.append(third_row)
            fourth_row = {
                "Columns": 6,
                "Rows": 1,
                "Text": f"<font color=#777777 size=12>{summary[:250]}</font>",
                "ActionType": "reply",
                "ActionBody": summary[:250],
                "TextSize": "medium",
                "TextVAlign": "middle",
                "TextHAlign": "right"
            }
            buttons.append(fourth_row)
        msg_obj = {
            "receiver": receiver,
            "type": "rich_media",
            "min_api_version": 2,
            "rich_media": {
                "Type": "rich_media",
                "ButtonsGroupColumns": 6,
                "ButtonsGroupRows": 7,
                "BgColor": "#FFFFFF",
                "Buttons": buttons
            }
        }

        return msg_obj
