# -*- encoding=utf8 -*-
__author__ = "wang"

from airtest.core.api import *
import time
import random
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

from gcjc.gcjc import *



    


#完成登录
def login(username='kentestgrp10',password='12345678',enterprise='p1'):
    
    
    #获取用户名输入框，点击清空内容并输入
    username_field = poco(text="请输入用户名") 
    username_field.click()
    username_field.set_text("") #不管有无值，设置text属性为空
    text(username,enter=False) #不自动换行

    #获取密码输入框，点击清空内容并输入(此步骤需要关闭安全键盘才能输入密码)
    password_field = poco(text="请输入密码")
    password_field.click()
    password_field.set_text("")
    text(password,enter=False)

    #获取企业码输入框，点击清空内容并输入
    enterprise_field = poco(text="企业编码(非必填)")
    enterprise_field.set_text("")
    enterprise_field.click()
    text(enterprise,enter=False)

    #获取登录按钮，点击登录
    login_button = poco(text="登录")
    login_button.click()
    
#清除app数据，等同于初次安装完成（无权限安装）
clear_app("cn.smartinspection.combine")

#启动指定app
start_app("cn.smartinspection.combine")

sleep(5)

#获取权限
authApp()

#等待启动完毕
sleep(5)

#登陆

login()
