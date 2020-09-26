# -*- encoding=utf8 -*-
__author__ = "zijie"
__title__ = "安卓端图纸文档模块回归测试报告"
__DESC__ = """
回归测试内容：
1.
2.
3.
"""


from airtest.core.api import *
import threading
import time
import random
import traceback
import os
import sys
import unittest
from airtest.report.report import simple_report


#导入上一层公共模块方法
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from login.login import *
from common_api.common_api import *

#导入最上级设置
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
from init_setting import *


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__, logdir=docs_logdir, devices=[
            "Android:///"])









class TestSafetyinspection(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #clear_app(apk)

        start_app(apk)
        sleep(2)
        
        #authApp()

        login('kentest50','12345678','p1','kentest50')
        
        selectMode("组织架构聚合")
        
        selectOrg_0(org_name='公司1项目贰')
        selectApp("图纸文档")        
    
    @classmethod
    def tearDownClass(cls):
        simple_report(filepath=os.path.realpath(__file__), logpath=docs_logdir, logfile=logfile, output=docs_output)

    def setUp(self):
        print("开始跑一个用例")

    def tearDown(self):
        print ("结束一个测试")
    def test_01_draw_manage():
    	print("图纸文档测试")

        
if __name__ == '__main__':
    unittest.main()