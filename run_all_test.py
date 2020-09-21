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

	#https://blog.csdn.net/Longtermevolution/article/details/105314149
	t2 = threading.Thread(target=networdTest)
	threads.append(t2)
	t2.setDaemon(True)  #线程t2无限循环判断，需要设置为守护线程(且不能调用join方法，join方法会阻塞父线程)，否则无法停止

	t1.start()     #t1为非守护线程，父线程执行完会等待所有非守护线程执行完才退出父线程，不管守护线程是否执行完（子线程未调用join的情况下）
	t2.start()

	print("开始测试")


	    
	#simple_report(filepath="run_all_test.py", logpath=logdir, logfile=logfile, output=output)