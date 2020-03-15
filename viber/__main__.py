import asyncio
from aiohttp import web
from viber.utils.webserver import web_server
from viber.utils.common import ViberCommon
from viber.utils.api.request_sender import ViberApiRequestSender


async def main():
    runner = web.AppRunner(await web_server())
    await runner.setup()
    await web.TCPSite(runner, '0.0.0.0', 8080).start()

    await asyncio.sleep(2)
    web_hook_payload = {
        'auth_token': ViberCommon.viber_auth_token,
        "url": ViberCommon.viber_web_hook_url,
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

    await ViberApiRequestSender().post('web_hook', web_hook_payload)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_forever()
