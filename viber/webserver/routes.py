import logging
from aiohttp import web
from viber.api.request_sender import ViberApiRequestSender
from viber.api.hadlers import ViberHandlers
routes = web.RouteTableDef()


@routes.post("/")
async def root_route_post_handler(request):
    received_data = await request.json()
    received_data_text = await request.text()
    received_signature = request.headers.get('X-Viber-Content-Signature')

    logging.info(await request.json())
    if await ViberApiRequestSender().validate_signature(received_signature, received_data_text):
        await ViberHandlers().on_event(received_data)
    else:
        logging.warn('Unauthorized request has been sent.')

    return web.Response(status=200)
