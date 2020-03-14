import configparser

import viber_client
from aiohttp import web

config = configparser.ConfigParser()
config.read('config.ini')

routes = web.RouteTableDef()
auth_token = config.get("viber", "auth_token")


@routes.post("/")
async def root_route_post_handler(request):
    print(await request.json())
    print(request.headers.get('X-Viber-Content-Signature'))

    received_data_json = await request.json()
    data_signature = request.headers.get('X-Viber-Content-Signature')
    received_data_text = await request.text()

    if await viber_client.verify_data(received_data_text, auth_token, data_signature):
        await viber_client.check_event(received_data_json, auth_token)
    else:
        print('Unauthorized Request')

    return web.Response(status=200)


@routes.get("/")
async def root_route_get_handler(request):
    payload = {
        'auth_token': auth_token,
        "url": "https://471040f1.ngrok.io",
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
    await viber_client.viber_post(
        uri="https://chatapi.viber.com/pa/set_webhook",
        payload=payload
    )
    return web.Response(status=200, body="")
