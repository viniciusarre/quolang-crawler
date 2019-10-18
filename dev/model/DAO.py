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
            self.writeLog('insertionError', e)
            Logger().error(str(e))

            sys.exit(1)

    def getData(self):
        r = []
        try:
            for d in self.db.quote.find():
                r.append(d)
            return r

        except Exception as e:
            self.writeLog('fetchinDataError', e)
            Logger().error(str(e))

    def checkAuthor(self, name):
        dt = []
        for i in self.db.quote.find({'url_name': name}):
            dt.append(i)
        return dt

    def writeLog(self, logType, log):
        print('logging... ')
        dt = self.findLog(logType)
        if dt:
            dt['logs'].append(log)
            self.db.log.update({'_id': dt['_id']},
                               {"$set": {'data': str(date.fromtimestamp(time.time())), 'type': logType,
                                         'logs': dt['logs']}})
        else:
            id = random.randint(1000, 50000)
            dt = self.getLog()
            if dt == True:
                id = int(dt[-1]['_id'])
            self.db.log.insert(
                {'_id': id + 1000, 'data': str(date.fromtimestamp(time.time())), 'type': logType, 'logs': [log]})

    def findLog(self, type):
        r = None
        for d in self.db.log.find({'type': type}):
            r = d
        return r

    def getLog(self):
        r = []
        try:
            if self.db.log.find():
                for d in self.db.log.find():
                    r.append(d)
            else:
                return []
        except Exception as e:
            self.writeLog('error', e)
            Logger().error(str(e))
