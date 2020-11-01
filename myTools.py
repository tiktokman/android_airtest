# -*- encoding=utf8 -*-
__author__ = "hallo"

import os

def clear_log():
	"""清理日志文件"""
	try:
		fileDir = os.path.dirname(os.path.realpath(__file__)) +'\log'    
		for root, dirs, files in os.walk(fileDir):  
			for name in files:
				os.remove(os.path.join(root, name))

	except Exception as e:
		print(e)
		raise
	else:
		print ("完成日志清理")
	finally:
		pass

if __name__ == '__main__':
	
	clear_log()