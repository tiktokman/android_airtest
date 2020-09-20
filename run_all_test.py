# -*- encoding=utf8 -*-
__author__ = "hallo"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import unittest
from airtest.report.report import simple_report
from init_setting import *
import threading
from exception import *

'''
if not cli_setup():
    auto_setup(__file__, logdir=logdir, devices=[
            "Android:///",
    ])


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
'''
def run_case():
	#设置用例路径，查找模块名称，导入匹配用例
	test_dir = project_root
	discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py',top_level_dir=None)

	runner = unittest.TextTestRunner()
	print (discover)
	runner.run(discover)




if __name__ == '__main__':
	"""清理日志文件"""
	'''
	fileDir = os.path.dirname(os.path.realpath(__file__)) +'\log'    
	for root, dirs, files in os.walk(fileDir):  
		for name in files:
			os.remove(os.path.join(root, name))
	print ("完成日志清理")
	'''

	threads = []

	t1 = threading.Thread(target=run_case)
	threads.append(t1)

	t2 = threading.Thread(target=networdTest)
	threads.append(t2)


	for t in threads:
	    t.setDaemon(True)
	    t.start()

	for t in threads:
	    print (t)
	    t.join()
	    
	#simple_report(filepath="run_all_test.py", logpath=logdir, logfile=logfile, output=output)