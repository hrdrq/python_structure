# -*- coding: utf-8 -*-

from hiro import Hiro

if __name__ == '__main__':
    h = Hiro('test')
    h.show_data()
    h.do_plus(1, 2)
    h.example_method()
    Hiro.example_class_method()
