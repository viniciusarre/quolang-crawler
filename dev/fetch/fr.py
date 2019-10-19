from dev.util.functions import format, filter
from dev.model.DAO import DAO
from dev.crawler.op import scrap
import sys


class French():
    d = None
    data = []
    url = 'https://fr.wikiquote.org/wiki/'

    def __init__(self):
        self.d = DAO()

    def fetch_data(self, data, soup, url_name):
        id = data[-1]['_id'] + 1 if len(data) > 0 else 1
        quotes= [filter(i.text)
                 for i in soup.findAll('div', {'class': 'citation'})]
        source = [filter(i.text)
                 for i in soup.findAll('div', {'class': 'ref'})]
        author = soup.find('h1', {'id': 'firstHeading'}).text
        aux = [{'quotes': quotes, 'source': source}]
        flag = "🇫🇷"
        data = format('fr', author, aux, flag,  url_name, id)
        return data

    def Fetch_Fr(self, soup, url_name):
        data = self.d.getData()
        data = self.fetch_data(data, soup, url_name)
        self.d.save(data)

    def urlSetUp(self, author, language):
        if len(self.d.checkAuthor(author)) > 0:
            status = 'All quotes from ' + author + ' in '+language+'  are up to date!'
            self.d.writeLog('status', status)
            print("Log registered!")
            return False
        else:
            print('****** formating url **** ')
            addr = self.url + author
            print(addr)
            self.Fetch_Fr(scrap(addr), author)
            return True
