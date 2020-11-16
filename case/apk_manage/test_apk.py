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
from airtest.core.android import *
from airtest.core.error import AirtestError
import threading
import traceback
import os
import sys
import pytest
from airtest.report.report import simple_report

#导入最上级设置
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
from init_setting import *



@pytest.fixture(scope="module",autouse=True)
def env_init():
	auto_setup(__file__, logdir=apkManage_logdir, devices=["Android:///"])
	print("完成环境初始化")

	yield
	simple_report(filepath=os.path.realpath(__file__), logpath=apkManage_logdir, logfile=logfile, output=apkManage_output)
	print("输出报告")
def call():
	android = Android()
	android.install_app(filepath=apkpath,replace=True)	
def allow_install():

    wait(Template(r"tpl1605543346543.png", record_pos=(-0.237, 0.858), resolution=(1080, 2340)),interval=1,timeout=20,intervalfunc=call)
    touch(Template(r"tpl1605543346543.png", record_pos=(-0.237, 0.858), resolution=(1080, 2340)))


def continue_install():


	t2 = threading.Thread(target=allow_install)
	t2.setDaemon(True)
	t2.start()

	#for i in range(100):
		#print("主线程：%s",i)
	try:
		android = Android()
		android.check_app(apk)
	
		print("当前设备已存在待安装应用，执行覆盖安装")
		android.install_app(filepath=apkpath,replace=False)
	except AirtestError:
		print("当前设备不存在待安装应用，执行覆盖安装")
		android.install_app(filepath=apkpath,replace=True)	


class TestApk():

	def test_installApp(self):
		continue_install()

if __name__ == '__main__':
    pytest.main(["-s","test_apk.py"])  