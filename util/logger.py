# -*- coding: utf-8 -*-i

import json
import logging
import datetime


class Logger:

    __monostate = None

    def __init__(self, name="quote-a-lang-crawler"):
        if not Logger.__monostate:

            log_format = ('{ "log_level": %(levelno)s, '
                          '"message": %(message)s }')

            self.logger = logging.getLogger(name)
            file_handler = logging.FileHandler(name + '.log')
            formatter = logging.Formatter(log_format)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

            self.logger.setLevel(logging.DEBUG)

        else:
            self.__dict__ = Logger.__monostate

    @staticmethod
    def __default(o):
        if type(o) is datetime.date or type(o) is datetime.datetime:
            return o.isoformat()

    def info(self, message, **kwargs):
        message_json = json.dumps(
            message, ensure_ascii=False, sort_keys=True, default=self.__default)
        self.logger.info(message_json, **kwargs)

    def success(self, message, **kwargs):
        message_json = json.dumps(
            message, ensure_ascii=False, sort_keys=True, default=self.__default)
        self.logger.info(message_json, **kwargs)

    def error(self, message, **kwargs):
        message_json = json.dumps(
            message, ensure_ascii=False, sort_keys=True, default=self.__default)
        self.logger.error(message_json, **kwargs)

    def critical(self, message, **kwargs):
        message_json = json.dumps(
            message, ensure_ascii=False, sort_keys=True, default=self.__default)
        self.logger.critical(message_json, **kwargs)

    def debug(self, message, **kwargs):
        message_json = json.dumps(
            message, ensure_ascii=False, sort_keys=True, default=self.__default)
        self.logger.debug(message_json, **kwargs)
