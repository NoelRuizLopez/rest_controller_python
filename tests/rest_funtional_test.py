'''
Created on 22 de nov. de 2016

@author: Asgard Team.Altran
'''
from __future__ import absolute_import
import unittest
from tests.utils_to_made_easy_testing.http_requests import HTTPRequests
from tests.utils_to_made_easy_testing.logger import Logger
from syntactic_analyzer.configuration.entry_points_URI import *
from syntactic_analyzer.configuration.error_codes import *

from rest_controller.configuration.read_config_file import get_config


_cfg = get_config()

TestLogName = "MainControllerTestLog"

class MainControllerTests(unittest.TestCase):

    def setUp(self):
        self.log = Logger(TestLogName)
        HTTPRequests.set_port(_cfg.port)

    def tearDown(self):
        self.log.release()

    def test_get_ok(self):
        msg = TestLogName + ' :: Test GET OK :: '

        result = HTTPRequests.GET(SERVICE_1)
        self.log.logResult(msg, CODE_GET_OK, result)

    def test_url_not_exists(self):
        msg = TestLogName + ' :: Test URL Does not exists :: '

        result = HTTPRequests.GET('/tests_wrong')
        self.log.logResult(msg, CODE_NOT_FOUND, result)

    def test_json_ok(self):
        msg = TestLogName + ' :: Test JSON OK :: '
        json = {"text":"El contenido de este texto es una prueba"}

        result = HTTPRequests.POST(SERVICE_2, json)

        self.log.logResult(msg, 200, result)


    '''
    def tearDown(self):


    def test_json_ok(self):


    def test_json_bad(self):


    def test_not_json(self):

    def test_tc_23_ok_only_mandatory(self):
        msg = TS + '023 Create Device:: Only Mandatory OK'
        print msg

        json = _device_only_mandatory_json(self.mac, self.ip_address)
        result = self.branch._create_device(json)

        self.logResult(msg, CODE_POST_OK, result)
        self.assertEqual(result.status_code, CODE_POST_OK, msg + ERROR)
'''

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.test']
    unittest.main()
