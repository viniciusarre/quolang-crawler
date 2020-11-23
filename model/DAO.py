from pymongo import MongoClient
from util.logger import Logger
import sys
import datetime
import random

logger = Logger()


class DAO:
    db = None

    def __init__(self):
        try:
            client = MongoClient("mongodb://localhost:27017")
            self.db = client.quotelang
        except Exception as e:
            logger.info('Connection error ' + e)

    def save(self, dic):
        try:
            self.db.quote.insert(dic)
            logger.info('data from ' + dic['author'] + ' in ' +
                        dic['language'] + ' added successfully!')
        except Exception as e:
            self.write_log('insertionError', e)
            logger.error(str(e))

            sys.exit(1)

    def get_data(self):
        r = []
        try:
            for d in self.db.quote.find():
                r.append(d)
            return r

        except Exception as e:
            self.write_log('fetchinDataError', e)
            logger.error(str(e))

    def check_author(self, name):
        dt = []
        for i in self.db.quote.find({'url_name': name}):
            dt.append(i)
        return dt

    def write_log(self, log_type, log):
        logger.info('logging... ')
        dt = self.__find_log(log_type)
        if dt:
            dt['logs'].append(log)
            self.db.log.update({'_id': dt['_id']},
                               {"$set": {'date': datetime.datetime.today(), 'type': log_type,
                                         'logs': dt['logs']}})
        else:
            id = random.randint(1000, 50000)
            dt = self.__get_log()
            if dt:
                id = int(dt[-1]['_id'])
            self.db.log.insert(
                {'_id': id + 1000, 'date': datetime.datetime.today(), 'type': log_type, 'logs': [log]})

    def __find_log(self, type):
        r = None
        for d in self.db.log.find({'type': type}):
            r = d
        return r

    def __get_log(self):
        r = []
        try:
            if self.db.log.find():
                for d in self.db.log.find():
                    r.append(d)
            else:
                return []
        except Exception as e:
            self.write_log('error', e)
            logger.error(str(e))
