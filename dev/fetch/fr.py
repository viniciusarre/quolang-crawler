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

    def Fetch_Fr(self, soup, url_name, save_to_db=True, data_in=[]):
        data = data_in
        if save_to_db:
            data = self.d.getData()
        id = data[-1]['_id'] + 1 if len(data) > 0 else 1
        quotes= [filter(i.text)
                 for i in soup.findAll('div', {'class': 'citation'})]
        source = [filter(i.text)
                 for i in soup.findAll('div', {'class': 'ref'})]
        author = soup.find('h1', {'id': 'firstHeading'}).text
        aux = [{'quotes': quotes, 'source': source}]
        flag = "🇫🇷"
        data = format('fr', author, aux, flag,  url_name, id)
        if save_to_db:
            self.d.save(data)

        return data

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
