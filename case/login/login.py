# -*- encoding=utf8 -*-
__author__ = "hallo"

from airtest.core.api import *
from airtest.core.helper import G
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from common_api.common_api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
#auto_setup(__file__)

basedir = os.path.dirname(os.path.abspath(__file__))
G.BASEDIR.append(basedir)




#完成登录 (首次打开登录页面，用户数据为空，输入账户登录，验证登陆成功后回到工作台)
def login(username='kentestgrp10',password='12345678',enterprise='p1',real_name='kentestgrp10'):
    poco.wait_for_any(poco(type='android.widget.EditText'))
    #遍历账号输入框，不管有没值，先置空
    for edittext in poco(type='android.widget.EditText'):
        edittext.set_text("")
    sleep(1)
    #获取用户名输入框，点击清空内容并输入
    username_field = poco(text="请输入用户名") 
    username_field.click()
    text(username,enter=False) #不自动换行

    #获取密码输入框，点击清空内容并输入(此步骤需要关闭安全键盘才能输入密码)
    password_field = poco(text="请输入密码")
    password_field.click()
    text(password,enter=False)

    #获取企业码输入框，点击清空内容并输入
    enterprise_field = poco(text="企业编码(非必填)")
    enterprise_field.click()
    text(enterprise,enter=False)

    #获取登录按钮，点击登录
    login_button = poco(text="登录")
    login_button.click()
    
    sleep(2)
    
    #网络异常登录重试
    while poco(text="重试"):
        poco(text="重试").click()
    
    
    #进入“我”工作栏
    selectTab("我")
    
    
    welcome_text = '你好，' + real_name
    sleep(1)
    if poco(text=welcome_text):
        print ("登录成功")
    else : assert_equal(1,0)  #否则登录失败
    assert_exists(Template(r"tpl1603007517626.png", record_pos=(0.008, 0.89), resolution=(1080, 2340)), "登录成功，进入app")
    
    sleep(1)
    #返回工作台
    selectTab("工作台")


#login('kentestgrp10','12345678','t8','kentest10')






