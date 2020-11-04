# -*- encoding=utf8 -*-
__author__ = "zijie"
__title__ = "包管理测试报告"
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
#import pytest
from airtest.report.report import simple_report

#导入最上级设置
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
from init_setting import *

auto_setup(__file__, logdir=docs_logdir, devices=["Android:///"])

#install(apkpath)
cmd = 'adb install -r -t -g '+apkpath
print(cmd)
shell('adb shell pm list packages -s')