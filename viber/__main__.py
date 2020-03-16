import asyncio
from aiohttp import web
from viber.utils.webserver import web_server
from viber.utils.api.msg_types import ViberMessageTypes
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from viber.utils.api.request_sender import ViberApiRequestSender
from viber.utils.database.majilis_collection import MajilisCollection
from viber.utils.database.gazette_collections import GazetteCollection
from viber.utils.helpers.scrapers import Scrapers


async def main():
    runner = web.AppRunner(await web_server())
    await runner.setup()
    await web.TCPSite(runner, '0.0.0.0', 8080).start()

    await asyncio.sleep(2)
    await ViberApiRequestSender().post('web_hook', await ViberMessageTypes().web_hook())

    scheduler = AsyncIOScheduler()
    scheduler.add_job(Scrapers().scrape_majilis, 'interval', hours=1)
    scheduler.add_job(Scrapers().scrape_gazatte, 'interval', hours=1)
    scheduler.start()

    """
    Initiate the DB for the first run
    """
    if not (await MajilisCollection().majilis_return_collection('bills_collection')):
        await Scrapers().scrape_majilis()
    if not (await GazetteCollection().gazette_return_collection()):
        await Scrapers().scrape_gazatte()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_forever()
