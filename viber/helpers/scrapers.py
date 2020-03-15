from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


class Scrapers:
    def __init__(self):
        self.bs = BeautifulSoup
        self.req = Request
        self.url_op = urlopen

    async def collect_bills(self):
        req = self.req('https://majlis.gov.mv/dv/19-parliament/parliament-works/type/1',
                       headers={'User-Agent': 'Mozilla/5.0'})
        page = self.url_op(req)
        soup = self.bs(page, 'html.parser')

        divs = soup.findAll('div', class_='col-12 my-3')

        bills = []
        for div in divs[:6]:
            data = div.findAll('a')
            for d in data[:6]:
                req = Request(d.get('href'),
                              headers={'User-Agent': 'Mozilla/5.0'})
                page = urlopen(req)
                soup = BeautifulSoup(page, 'html.parser')
                status = soup.find('li', class_='active')
                summary = soup.find('div', class_='max-600w').p
                bill = {
                    'name': d.text,
                    'link': d.get('href'),
                    'status': f"މިހާރު އޮތް ހިސާބް: {status.text.strip()}",
                    'summary': summary.text.strip()
                }
                bills.append(bill)

        return bills

    async def collect_resolutions(self):
        req = self.req('https://majlis.gov.mv/dv/19-parliament/parliament-works/type/2',
                       headers={'User-Agent': 'Mozilla/5.0'})
        page = self.url_op(req)
        soup = self.bs(page, 'html.parser')

        divs = soup.findAll('div', class_='col-12 my-3')

        resolutions = []
        for div in divs[:6]:
            data = div.findAll('a')
            for d in data[:6]:
                req = Request(d.get('href'),
                              headers={'User-Agent': 'Mozilla/5.0'})
                page = urlopen(req)
                soup = BeautifulSoup(page, 'html.parser')
                status = soup.find('li', class_='active')
                summary = soup.find('div', class_='max-600w').p
                bill = {
                    'name': d.text,
                    'link': d.get('href'),
                    'status': f"މިހާރު އޮތް ހިސާބް: {status.text.strip()}",
                    'summary': summary.text.strip()
                }
                resolutions.append(bill)

        return resolutions

    async def collect_emergency_debates(self):
        req = self.req('https://majlis.gov.mv/dv/19-parliament/parliament-works/type/4',
                       headers={'User-Agent': 'Mozilla/5.0'})
        page = self.url_op(req)
        soup = self.bs(page, 'html.parser')

        divs = soup.findAll('div', class_='col-12 my-3')

        emergency_debates = []
        for div in divs[:6]:
            data = div.findAll('a')
            for d in data[:6]:
                req = Request(d.get('href'),
                              headers={'User-Agent': 'Mozilla/5.0'})
                page = urlopen(req)
                soup = BeautifulSoup(page, 'html.parser')
                status = soup.find('li', class_='active')
                summary = soup.find('div', class_='max-600w').p
                bill = {
                    'name': d.text,
                    'link': d.get('href'),
                    'status': f"މިހާރު އޮތް ހިސާބް: {status.text.strip()}",
                    'summary': summary.text.strip()
                }
                emergency_debates.append(bill)

        return emergency_debates

    async def collect_approvals(self):
        req = self.req('https://majlis.gov.mv/dv/19-parliament/parliament-works/type/6',
                       headers={'User-Agent': 'Mozilla/5.0'})
        page = self.url_op(req)
        soup = self.bs(page, 'html.parser')

        divs = soup.findAll('div', class_='col-12 my-3')

        approvals = []
        for div in divs[:6]:
            data = div.findAll('a')
            for d in data[:6]:
                req = Request(d.get('href'),
                              headers={'User-Agent': 'Mozilla/5.0'})
                page = urlopen(req)
                soup = BeautifulSoup(page, 'html.parser')
                status = soup.find('li', class_='active')
                summary = soup.find('div', class_='max-600w').p
                bill = {
                    'name': d.text,
                    'link': d.get('href'),
                    'status': f"މިހާރު އޮތް ހިސާބް: {status.text.strip()}",
                    'summary': summary.text.strip()
                }
                approvals.append(bill)

        return approvals

    async def collect_others(self):
        req = self.req('https://majlis.gov.mv/dv/19-parliament/parliament-works/type/7',
                       headers={'User-Agent': 'Mozilla/5.0'})
        page = self.url_op(req)
        soup = self.bs(page, 'html.parser')

        divs = soup.findAll('div', class_='col-12 my-3')

        others = []
        for div in divs[:6]:
            data = div.findAll('a')
            for d in data[:6]:
                req = Request(d.get('href'),
                              headers={'User-Agent': 'Mozilla/5.0'})
                page = urlopen(req)
                soup = BeautifulSoup(page, 'html.parser')
                status = soup.find('li', class_='active')
                summary = soup.find('div', class_='max-600w').p
                bill = {
                    'name': d.text,
                    'link': d.get('href'),
                    'status': f"މިހާރު އޮތް ހިސާބް: {status.text.strip()}",
                    'summary': summary.text.strip()
                }
                others.append(bill)

        return others
