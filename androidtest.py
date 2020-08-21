# -*- encoding=utf8 -*-
__author__ = "hallo"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

import configparser
config = configparser.ConfigParser()
config.read("config.ini", encoding="utf-8")


'''
if not cli_setup():
    auto_setup(__file__, logdir="C:/log", devices=[
            "Android:///",
    ], project_root="C:/airtest_script")
'''

if not cli_setup():
    auto_setup(__file__, logdir="D:\log", devices=[
            "Android:///",
    ], project_root="D:/android_airtest")

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

using("common_api.air")
from common_api import *

using("safety_inspection.air")
from safety_inspection import *
       

import unittest
from airtest.report.report import simple_report


class TestAndroid(unittest.TestCase):
    
    def setUp(self):
        print("开始跑测试用例")

    def tearDown(self):
    	simple_report(filepath="androidtest.py", logpath="D:\log", logfile="log.txt", output="D:\log\log.html")
    	print ("结束一个测试")
    def test_print(self):
    	safetyInspection()
    def test_stop(self):

        stop_app('cn.smartinspection.combine')
        
if __name__ == '__main__':
    unittest.main()
# generate html report
# 命令行生成报告  airtest report androidtest.py --log_root D:\log\ --outfile D:\log\log.html --lang zh --plugin poco.utils.airtest.report
#from airtest.report.report import simple_report
#simple_report(__file__)
