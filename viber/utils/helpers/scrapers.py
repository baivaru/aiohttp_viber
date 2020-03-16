from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from viber.utils.database.majilis_collection import MajilisCollection


class Scrapers:
    def __init__(self):
        self.bs = BeautifulSoup
        self.req = Request
        self.url_op = urlopen

    async def scrape_majilis(self):
        for x in [1, 2, 4, 6, 7]:
            req = self.req(f'https://majlis.gov.mv/dv/19-parliament/parliament-works/type/{x}',
                           headers={'User-Agent': 'Mozilla/5.0'})
            page = self.url_op(req)
            soup = self.bs(page, 'html.parser')

            divs = soup.findAll('div', class_='col-12 my-3')

            for div in divs[:6]:
                data = div.findAll('a')
                for d in data[:6]:
                    req = Request(d.get('href'),
                                  headers={'User-Agent': 'Mozilla/5.0'})
                    page = urlopen(req)
                    soup = BeautifulSoup(page, 'html.parser')
                    status = soup.find('li', class_='active')
                    summary = soup.find('div', class_='max-600w').p

                    collection = None
                    if x == 1:
                        collection = 'bills_collection'
                    elif x == 2:
                        collection = 'resolutions_collection'
                    elif x == 4:
                        collection = 'emergency_debates_collection'
                    elif x == 6:
                        collection = 'approvals_collection'
                    elif x == 7:
                        collection = 'others_collection'

                    await MajilisCollection().majilis_updates_from_scheduler(collection=collection,
                                                                             name=d.text,
                                                                             link=d.get('href'),
                                                                             status=f"މިހާރު އޮތް ހިސާބް: {status.text.strip()}",
                                                                             summary=summary.text.strip())
