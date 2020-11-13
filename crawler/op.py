import requests
import sys
from bs4 import BeautifulSoup

from model.DAO import DAO
from util.logger import Logger


def scrap(url):
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html.parser")
        return soup
    else:
        d = DAO()
        d.write_log('crawlerError',  str(r.status_code) + ' ' + url)
        Logger().error(str(r.status_code) + ' ' + url)
        print('registered connection error!',
              str(r.status_code) + ' ' + url)
        sys.exit(1)
