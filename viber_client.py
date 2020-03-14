import hmac
import hashlib
import aiohttp


async def viber_post(uri, payload):
    headers = {
        'User-Agent': "ViberBot-Python/0.0.1"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url=uri, json=payload, headers=headers) as resp:
            print(await resp.text())


async def verify_data(data, auth_token, signature):
    calculated_signature = hmac.new(
        bytes(auth_token.encode('ascii')),
        msg=str(data).encode(),
        digestmod=hashlib.sha256).hexdigest()
    return calculated_signature == signature


async def check_event(data, auth_token):
    if data['event'] == 'subscribed':
        await send_welcome(data, auth_token)
    elif data['event'] == 'unsubscribed':
        pass
    elif data['event'] == 'conversation_started':
        pass
    elif data['event'] == 'message':
        await on_message(data, auth_token)


async def send_welcome(data, auth_token):
    payload = {
        'auth_token': auth_token,
        "receiver": data["user"]["id"],
        "min_api_version": 1,
        "sender": {
            "name": "vakkarubutler",
            "avatar": "https://i1.sndcdn.com/avatars-000237096059-ymz7kd-t500x500.jpg"
        },
        "tracking_data": "tracking data",
        "type": "text",
        "text": "Hello world!"
    }
    await viber_post(
        uri="https://chatapi.viber.com/pa/send_message",
        payload=payload
    )


async def on_message(data, auth_token):
    if data['message']['type'] == 'text':
        if (data['message']['text']) == '!test':
            text = 'user issued the command test'
        else:
            text = data['message']['text']
        payload = {
            'auth_token': auth_token,
            "receiver": data["sender"]["id"],
            "min_api_version": 1,
            "sender": {
                "name": "vakkarubutler",
                "avatar": "https://i1.sndcdn.com/avatars-000237096059-ymz7kd-t500x500.jpg"
            },
            "tracking_data": "tracking data",
            "type": "text",
            "text": text
        }
        await viber_post(
            uri="https://chatapi.viber.com/pa/send_message",
            payload=payload
        )