# -*- encoding=utf8 -*-
__author__ = "hallo"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import func_timeout
import pytest
from airtest.report.report import simple_report
from init_setting import *

#超时处理   https://blog.csdn.net/weixin_39858881/article/details/107152961

@func_timeout.func_set_timeout(10)
def askModule():
	test_id = input("请在10s内输入要执行测试的模块,使用空格分隔：").split(' ')
	return test_id

def output_args():
	module = {"所有模块":{"0":"all"},"图纸文档":{"1":"docs"},"包管理":{"2":"apk"},"安全检查":{"3":"safety_inspection"}}
	print("  模块-----------编号")

	for module_name in module:
		for module_id in module[module_name]:
			print(module_name+" "*(20-len(module_name)*2)+module_id)
	try:
		test_id =askModule()
	except func_timeout.exceptions.FunctionTimedOut as e:
		test_id = ["0"]

	test_module = []

	if '0' in test_id:
		print("运行所有模块")
		args = "./"
		return args
	else:
		for module_name in module:
			for module_id in module[module_name]:
				if module_id in test_id:
					test_module.append(module[module_name][module_id])
		args = " or ".join(test_module)
		return args

if __name__ == '__main__':
	
	#pytest.main(["-v","-s","-m","docs and apk"])

	args=output_args()

	if args =="./":
		pytest.main(["-v","-s","./"])

	else:
		pytest.main(["-v","-s","-m",args])





