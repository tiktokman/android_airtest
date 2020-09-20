# -*- encoding=utf8 -*-
__author__ = "hallo"

from airtest.core.api import *
import threading
import time
import random
import traceback
import os
import sys
import unittest
from airtest.report.report import simple_report
from init_setting import *






def networdTest():
	from poco.drivers.android.uiautomation import AndroidUiautomationPoco
	poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


	#auto_setup(__file__)
	#网络异常登录重试
	while True:
		if poco(text="登录").exists():  #检测到弹窗出现，应先停止掉其他线程的运行
			poco(text="登录").click()
			print("网络测试")
			sleep(1)

