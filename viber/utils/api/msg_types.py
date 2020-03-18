import os
import aiofiles
import aiohttp
from viber.utils.common import ViberCommon


class ViberMessageTypes:
    def __init__(self):
        self.sender_name = ViberCommon.viber_name,
        self.sender_avatar = ViberCommon.viber_avatar,
        self.auth_token = ViberCommon.viber_auth_token
        self.web_hook_url = ViberCommon.viber_web_hook_url

    async def web_hook(self):
        web_hook_object = {
            'auth_token': self.auth_token,
            "url": self.web_hook_url,
            "event_types": [
                "delivered",
                "seen",
                "failed",
                "subscribed",
                "unsubscribed",
                "conversation_started"
            ],
            "send_name": True,
            "send_photo": True
        }

        return web_hook_object

    async def text_message(self, receiver, text, tracking_data, keyboard):
        msg_obj = {
            "receiver": receiver,
            "min_api_version": 1,
            "sender": {
                "name": self.sender_name,
                "avatar": self.sender_avatar
            },
            "tracking_data": tracking_data,
            "type": "text",
            "text": text
        }
        if keyboard is not None:
            msg_obj['keyboard'] = keyboard

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

    async def file_message(self, receiver, url, tracking_data, keyboard):
        """
        We download the file here since the headers doesnt come with content length. file size is a
        mandatory field while sending files
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                headers = resp.headers
                filename = headers['Content-Disposition'].split('; ')[1].replace('filename=', '').replace('"', '')
                tmp_file = os.path.join('viber/working_dir/', filename)

                downloaded_size = 0
                async with aiofiles.open(tmp_file, mode='wb') as f:
                    async for chunk in resp.content.iter_chunked(1024):
                        if chunk:
                            f.write(chunk)
                            downloaded_size += len(chunk)

                file_size = downloaded_size

                if os.path.exists(tmp_file):
                    os.remove(tmp_file)

                msg_obj = {
                    "receiver": receiver,
                    "min_api_version": 1,
                    "sender": {
                        "name": self.sender_name,
                        "avatar": self.sender_avatar
                    },
                    "tracking_data": tracking_data,
                    "type": "file",
                    "media": url,
                    "size": file_size,
                    "file_name": filename
                }

                if keyboard is not None:
                    msg_obj['keyboard'] = keyboard

                return msg_obj

    async def picture_message(self, receiver, text, media, thumb, tracking_data, keyboard):
        msg_obj = {
            "receiver": receiver,
            "min_api_version": 1,
            "sender": {
                "name": self.sender_name,
                "avatar": self.sender_avatar
            },
            "tracking_data": tracking_data,
            "type": "picture",
            "text": text,
            "media": media,
            "thumbnail": thumb
        }

        if keyboard is not None:
            msg_obj['keyboard'] = keyboard

        return msg_obj

    async def video_message(self, receiver, media, size, thumbnail, duration, tracking_data, keyboard):
        msg_obj = {
            "receiver": receiver,
            "min_api_version": 1,
            "sender": {
                "name": self.sender_name,
                "avatar": self.sender_avatar
            },
            "tracking_data": tracking_data,
            "type": "video",
            "media": media,
            "thumbnail": thumbnail,
            "size": size,
            "duration": duration
        }

        if keyboard is not None:
            msg_obj['keyboard'] = keyboard

        return msg_obj

    async def location_message(self):
        msg_obj = {
            "receiver": "01234567890A=",
            "min_api_version": 1,
            "sender": {
                "name": "John McClane",
                "avatar": "http://avatar.example.com"
            },
            "tracking_data": "tracking data",
            "type": "location",
            "location": {
                "lat": "37.7898",
                "lon": "-122.3942"
            }
        }
