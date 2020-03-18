from viber.utils.common import ViberCommon
from viber.utils.api.commands import ViberCommands
from viber.utils.api.msg_types import ViberMessageTypes
from viber.utils.api.request_sender import ViberApiRequestSender
from viber.utils.database.gazette_collections import GazetteCollection
from viber.utils.helpers.foursqure import FourSquare
from viber.utils.api.keyboards import ViberKeyboards


class ViberTrackingDataAttendant:
    def __init__(self):
        self.sender_name = ViberCommon.viber_name
        self.sender_avatar = ViberCommon.viber_avatar

    async def attend(self, tracking_data, data):
        message = data['message']['text'] if 'text' in data['message'] else None
        message_type = data['message']['type']
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
        elif tracking_data == 'foursquare':
            if message_type != 'location':
                if message != '!negatenearme':
                    message = await ViberMessageTypes().sticker_message(receiver, 20818, None, None)
                    payload = await ViberCommands().prepare_payload(message=message,
                                                                    sender_name=self.sender_name,
                                                                    sender_avatar=self.sender_avatar,
                                                                    sender=None,
                                                                    receiver=receiver,
                                                                    chat_id=None)
                    await ViberApiRequestSender().post('send_message', payload)
                    message = await ViberMessageTypes().text_message(receiver,
                                                                     "I asked for your location not a "
                                                                     "text message, send me the location as a "
                                                                     "location Message, you can not do this on a PC! "
                                                                     "To cancel this send me the command !negatenearme",
                                                                     'foursquare',
                                                                     None)
                    payload = await ViberCommands().prepare_payload(message=message,
                                                                    sender_name=self.sender_name,
                                                                    sender_avatar=self.sender_avatar,
                                                                    sender=None,
                                                                    receiver=receiver,
                                                                    chat_id=None)
                    await ViberApiRequestSender().post('send_message', payload)
                else:
                    message = await ViberMessageTypes().text_message(receiver,
                                                                     "Successfully negated finding nearby venues..",
                                                                     None,
                                                                     None)
                    payload = await ViberCommands().prepare_payload(message=message,
                                                                    sender_name=self.sender_name,
                                                                    sender_avatar=self.sender_avatar,
                                                                    sender=None,
                                                                    receiver=receiver,
                                                                    chat_id=None)
                    await ViberApiRequestSender().post('send_message', payload)
            else:
                location = data['message']['location']
                venues = await FourSquare().sear_near_by(location)
                foursquare_keyboard = await ViberKeyboards().foursquare_keyboard(venues)
                message = await ViberMessageTypes().text_message(receiver,
                                                                 'Here are the venues I found nearby',
                                                                 'foursquare_keyboard',
                                                                 foursquare_keyboard)
                payload = await ViberCommands().prepare_payload(message=message,
                                                                sender_name=self.sender_name,
                                                                sender_avatar=self.sender_avatar,
                                                                sender=None,
                                                                receiver=receiver,
                                                                chat_id=None)
                await ViberApiRequestSender().post('send_message', payload)
        elif tracking_data == 'foursquare_keyboard':
            split_data = str(message).split(",")
            lat = split_data[0]
            lon = split_data[1]
            contact = split_data[2]
            name = split_data[3]

            message = await ViberMessageTypes().location_message(receiver, lat, lon, None, None)
            payload = await ViberCommands().prepare_payload(message=message,
                                                            sender_name=self.sender_name,
                                                            sender_avatar=self.sender_avatar,
                                                            sender=None,
                                                            receiver=receiver,
                                                            chat_id=None)
            await ViberApiRequestSender().post('send_message', payload)
            if contact != 'None':
                message = await ViberMessageTypes().contact_message(receiver, name, contact, None, None)
                payload = await ViberCommands().prepare_payload(message=message,
                                                                sender_name=self.sender_name,
                                                                sender_avatar=self.sender_avatar,
                                                                sender=None,
                                                                receiver=receiver,
                                                                chat_id=None)
                await ViberApiRequestSender().post('send_message', payload)

        else:
            message = await ViberMessageTypes().sticker_message(receiver, 32917, None, None)
            payload = await ViberCommands().prepare_payload(message=message,
                                                            sender_name=self.sender_name,
                                                            sender_avatar=self.sender_avatar,
                                                            sender=None,
                                                            receiver=receiver,
                                                            chat_id=None)
            await ViberApiRequestSender().post('send_message', payload)