# -*- encoding=utf8 -*-
__author__ = "wang"

import unittest

from airtest.core.api import *

#ST.PROJECT_ROOT = "D:\\airtest_script\\"
ST.PROJECT_ROOT = "D:\\android_airtest\\"

from airtest.core.api import using

using("safety_inspection.air")
from safety_inspection import safetyInspection

auto_setup(__file__)


class androidTestCase(unittest.TestCase):
    
    def setUp(self):
        '''执行每个用例前默认调用'''
        connect_device("Android:///")
        apk = "cn.smartinspection.combine"
        clear_app("cn.smartinspection.combine")

        start_app(apk)
        
    def test_safetyInspection(self):
        stop_app("cn.smartinspection.combine")
            
    def test_print(self):
        print ("22222222")
            
if __name__ == '__main__':
    unittest.main()
    
    