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
from airtest.core.helper import G
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

#G.DEVICE.install_app(apkpath,install_options='-r -t -g')
cmd = 'adb install -r -t -g '+apkpath
print(cmd)

shell('pm list packages -3')

'''
    def install_app(self, filepath, replace=False, install_options=None):
        """
        Install the application on the device

        Args:
            filepath: full path to the `apk` file to be installed on the device
            replace: True or False to replace the existing application
            install_options: list of options, default is []

        Returns:
            output from installation process

        """
        return self.adb.install_app(filepath, replace=replace, install_options=install_options)
'''
