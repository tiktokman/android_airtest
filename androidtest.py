# -*- encoding=utf8 -*-
__author__ = "hallo"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir="C:/log", devices=[
            "Android:///",
    ], project_root="C:/airtest_script")

using("common_api.air")
from common_api import *
    
    
# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath="C:/log")

import unittest

class TestAndroid(unittest.TestCase):
    
    def setUp(self):
        print("11111111")
        clear_app('cn.smartinspection.combine')
    def test_print(self):
        print("22222222")
        start_app('cn.smartinspection.combine')
        authApp()
    def test_stop(self):
        print("33333333")
        stop_app('cn.smartinspection.combine')
        
if __name__ == '__main__':
    unittest.main()