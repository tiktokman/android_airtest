# -*- encoding=utf8 -*-
__author__ = "hallo"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import unittest
from airtest.report.report import simple_report
from init_setting import *

if not cli_setup():
    auto_setup(__file__, logdir=logdir, devices=[
            "Android:///",
    ], project_root=project_root)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)



test_dir = r'C:\airtest_script\case'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_safety_*.py',top_level_dir=None)

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    print (discover)
    runner.run(discover)
    simple_report(filepath="run_all_test.py", logpath=logdir, logfile=logfile, output=output)