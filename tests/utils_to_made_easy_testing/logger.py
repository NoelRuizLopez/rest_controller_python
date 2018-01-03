'''
Created on 20 de dic. de 2016

@author: Asgard Team.Altran
'''

from logging import FileHandler
import logging

import unittest

ERROR = ' - Error'


class Logger( unittest.TestCase):

    def __init__(self, filename):
        self.prepare_logger(filename)
        print '---------------------------------------------------------------'

    def prepare_logger(self, filename):
        self.logger = logging.getLogger('NBI:')
        self.logger.setLevel(logging.INFO)
        self.getHdlr(filename)
        self.logger.addHandler(self.hdlr)

    def getHdlr(self, filename):
        self.hdlr = FileHandler("/tmp/" + filename + "log")
        _format = '%(asctime)s::%(levelname)s::%(message)s'
        _datefmt = '%Y/%m/%d %H:%M:%S'
        self.hdlr.setFormatter(logging.Formatter(_format, datefmt=_datefmt))

    def release_logger(self):
        self.logger.removeHandler(self.hdlr)
        self.hdlr.close()

    def logResult(self, test, expected, result):
        level = logging.INFO if str(expected) in ["N.A."] or \
                                expected == result.status_code else logging.ERROR
        self.logger.log(level, test + ".\t" + \
                        "Expected:" + str(expected) + ".\t" + \
                        "Returned: " + str(result.status_code) + ".")
        if result._content is not None:
            self.logger.log(level, "\t" + str(result._content))


    def release(self):
        self.release_logger()


if __name__ == "__main__":
    unittest.main()
