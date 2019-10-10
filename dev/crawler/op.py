import requests
from bs4 import BeautifulSoup
from dev.model.DAO import DAO
import sys


def scrap(url):
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, "html.parser")
        return soup
    else:
        d = DAO()
        d.writeLog('crawlerError',  str(r.status_code) + ' ' + url)
        print('registered connection error!',
              str(r.status_code) + ' ' + url)
        sys.exit(1)
