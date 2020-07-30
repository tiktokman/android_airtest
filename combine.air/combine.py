# -*- encoding=utf8 -*-
__author__ = "hallo"

ST.PROJECT_ROOT = "C:\\airtest_script\\"  #公司电脑路径
#ST.PROJECT_ROOT = "D:\\android_airtest\\"   #个人电脑路径


from airtest.core.api import *
import unittest
auto_setup(__file__)

class TestAndroid(unittest.TestCase):
    
    def setup(self):
        print("11111111")
        
    def test_print(self):
        print("22222222")
        
if __name__ == '__main__':
    unittest.main()