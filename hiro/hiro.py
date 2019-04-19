# -*- coding: utf-8 -*-

from hiro.base import Base
from hiro.utility import plus
from hiro.method import example_class_method

class Hiro(Base):

    from hiro.method import example_method

    def __init__(self, data):
        super().__init__()
        self.data = data

    def show_data(self):
        self.log_info(self.data)

    def do_plus(self, a, b):
        self.log_info(plus(a, b))

Hiro.example_class_method = classmethod(example_class_method)
