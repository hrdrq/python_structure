# -*- coding: utf-8 -*-
from logging import Formatter, handlers, getLogger, StreamHandler, DEBUG


class Base(object):

    def __init__(self):
        logger = getLogger(__name__)
        logger.setLevel(DEBUG)
        formatter = Formatter('[%(asctime)s][%(levelname)s]%(message)s')
        handler = StreamHandler()
        handler.setLevel(DEBUG)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        self.logger = logger

    def log_info(self, text):
        self.logger.info(text)
