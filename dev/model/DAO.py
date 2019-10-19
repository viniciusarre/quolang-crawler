from pymongo import MongoClient
from dev.util.logger import Logger
import sys
import time
from datetime import date
import random


class DAO:
    db = None

    def __init__(self):
        try:
            client = MongoClient("mongodb://localhost:27017")
            self.db = client.quotelang
        except Exception as e:
            print('Connection error ' + e)

    def save(self, dic):
        try:
            self.db.quote.insert(dic)
            print('data from ' + dic['author'] + ' in ' +
                  dic['language'] + ' added successfully!')
        except Exception as e:
            self.write_log('insertionError', e)
            Logger().error(str(e))

            sys.exit(1)

    def get_data(self):
        r = []
        try:
            for d in self.db.quote.find():
                r.append(d)
            return r

        except Exception as e:
            self.write_log('fetchinDataError', e)
            Logger().error(str(e))

    def check_author(self, name):
        dt = []
        for i in self.db.quote.find({'url_name': name}):
            dt.append(i)
        return dt

    def write_log(self, log_type, log):
        print('logging... ')
        dt = self.__find_log(log_type)
        if dt:
            dt['logs'].append(log)
            self.db.log.update({'_id': dt['_id']},
                               {"$set": {'data': str(date.fromtimestamp(time.time())), 'type': log_type,
                                         'logs': dt['logs']}})
        else:
            id = random.randint(1000, 50000)
            dt = self.__get_log()
            if dt:
                id = int(dt[-1]['_id'])
            self.db.log.insert(
                {'_id': id + 1000, 'data': str(date.fromtimestamp(time.time())), 'type': log_type, 'logs': [log]})

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
            Logger().error(str(e))
