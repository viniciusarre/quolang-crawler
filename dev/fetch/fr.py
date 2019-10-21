from dev.util.functions import format, filter
from dev.model.DAO import DAO
from dev.crawler.op import scrap
from dev.util.logger import Logger


class French:

    d = None
    data = []
    url = 'https://fr.wikiquote.org/wiki/'

    def __init__(self):
        self.d = DAO()

    def __fetch_fr(self, soup, url_name, save_to_db=True, data_in=[]):
        data = data_in
        if save_to_db:
            data = self.d.get_data()
        id = data[-1]['_id'] + 1 if len(data) > 0 else 1
        quotes = [filter(i.text) for i in soup.findAll('div', {'class': 'citation'})]
        source = [filter(i.text) for i in soup.findAll('div', {'class': 'ref'})]
        author = soup.find('h1', {'id': 'firstHeading'}).text
        aux = [{'quotes': quotes, 'source': source}]
        flag = "🇫🇷"
        data = format('fr', author, aux, flag,  url_name, id)
        if save_to_db:
            self.d.save(data)

        return data

    def url_set_up(self, author, language, save_to_db=True,
                    data_in=[], author_in=[]):
        author_data = author_in
        if save_to_db:
            author_data = self.d.check_author(author)

        if len(author_data) > 0:
            status = 'All quotes from ' + author + ' in '+language+'  are up to date!'
            if save_to_db:
                self.d.write_log('status', status)
            Logger().info(status)
            print("Log registered!")
            return {
                "status": False,
                "result": {}
            }
        else:
            print('****** formating url **** ')
            addr = self.url + author
            print(addr)
            data = self.__fetch_fr(scrap(addr), author,
                                    save_to_db=save_to_db, data_in=data_in)
            return {
                "status": True,
                "result": data
            }
