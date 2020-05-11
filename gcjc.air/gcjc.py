# -*- encoding=utf8 -*-
__author__ = "wang"

from airtest.core.api import *






auto_setup(__file__)

import time
import random
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


    
def authApp():
    
    while poco(text="允许"):
        poco(text="允许").click()
        sleep(0.5)


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

    
#应用页进入项目工程检查模块并完成数据加载,进入任务   
def enter_gcjc():
#等待登录完成知道加载完页面内容
    from poco.drivers.android.uiautomation import AndroidUiautomationPoco
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    wait(Template(r"tpl1568706376007.png", record_pos=(0.005, -0.784), resolution=(1080, 2340)))


    input_label = poco(text="请输入关键词")
    input_label.click()
    text("公司1项目贰",enter=False) #搜索10

    sleep(1) #延迟一秒，等待搜索结果

    #进入安全检查

    touch(Template(r"tpl1568706562070.png", record_pos=(0.344, 0.218), resolution=(1080, 2340)))
    
    if exists(Template(r"tpl1554701332898.png", record_pos=(-0.002, 0.596), resolution=(1080, 2244))):
        touch(Template(r"tpl1554701345132.png", record_pos=(0.002, 0.585), resolution=(1080, 2244)))
        
    sleep(3)
    if exists(Template(r"tpl1554780545722.png", record_pos=(0.29, -0.89), resolution=(1080, 2244))):
        touch(Template(r"tpl1554701394682.png", record_pos=(0.38, -0.887), resolution=(1080, 2244)))





    if exists(Template(r"tpl1554781024060.png", record_pos=(0.35, -0.887), resolution=(1080, 2244))):
        sleep(2)

    wait(Template(r"tpl1554781049671.png", record_pos=(0.348, -0.89), resolution=(1080, 2244)),timeout=120) #加载完成
    sleep(2)

    poco(text="迁移回归0527").click() #点击进入安全检查2019任务 text的值区分任务

    

#进入任务后
#清单模式
#新增问题
def list_add_issue():
    wait(Template(r"tpl1554454159324.png", record_pos=(0.016, 0.976), resolution=(1080, 2244))) #等待加载完出现指派新增按钮

    touch(Template(r"tpl1554454246578.png", record_pos=(0.267, 0.974), resolution=(1080, 2244)))

    touch(Template(r"tpl1568708080199.png", record_pos=(-0.256, -0.769), resolution=(1080, 2340)))


    touch(Template(r"tpl1554454352019.png", record_pos=(-0.35, -0.419), resolution=(1080, 2244)))
    
    wait(Template(r"tpl1554702440180.png", record_pos=(-0.002, 0.81), resolution=(1080, 2244)))
    sleep(1)


    touch(Template(r"tpl1554454378918.png", record_pos=(0.005, 0.81), resolution=(1080, 2244)))
    
    sleep(2)

    swipe((200,1000),(1000,1000),duration=1) #从左到右画横线1秒
    sleep(1)
    swipe((500,700),(500,1500),duration=1) #从上到下画横线1秒

    touch(Template(r"tpl1554454924528.png", record_pos=(0.43, -0.878), resolution=(1080, 2244)))
    
    sleep(1)
    touch((156,700))  #点击图片位置查看图片
    
    pinch(in_or_out='out',center=(500,1300),percent=0.005)  #放大
    pinch(in_or_out='in',center=(500,1300),percent=0.005)   #缩小
    sleep(1)
    
    #poco("cn.smartinspection.combine:id/a5v").click()#查看定位
    touch(Template(r"tpl1568708907804.png", record_pos=(-0.464, 0.832), resolution=(1080, 2340)))

    sleep(1)
    pinch(in_or_out='out',center=(500,1300),percent=0.005)  #放大
    sleep(0.5)
    pinch(in_or_out='in',center=(500,1300),percent=0.005)  
    sleep(1)
    
     #poco("android.widget.ImageView").click() #退出地图页
    touch(Template(r"tpl1571304212660.png", record_pos=(-0.368, -0.906), resolution=(1080, 2340)))
    
    poco("转到上一层级").click()





    touch(Template(r"tpl1554454943328.png", record_pos=(-0.337, -0.193), resolution=(1080, 2244)))

    #选择检查项，目前都是选择固定检查项（此处使用poco可做优化改为随机选择）
    
    import random
    from poco.drivers.android.uiautomation import AndroidUiautomationPoco
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    
    #获取检查项列表（一个任务只有一份检查项）
    while poco(desc="搜索"):  #只要还有搜索按钮表明未选完检查项
        check_item = poco("cn.smartinspection.combine:id/xx").offspring("cn.smartinspection.combine:id/ady")
        #item_name = check_item[random.randint(0,len(check_item)-1)].get_text()
        #poco(text=item_name).click()
        poco(text=check_item[random.randint(0,len(check_item)-1)].get_text()).click()
        sleep(1)

    sleep(1)
    touch(Template(r"tpl1554461212564.png", record_pos=(-0.298, 0.092), resolution=(1080, 2244)))

    sleep(5)

    touch(Template(r"tpl1554461236054.png", record_pos=(0.003, -0.055), resolution=(1080, 2244)))
    touch(Template(r"tpl1554461254955.png", record_pos=(0.031, 0.294), resolution=(1080, 2244)))
    
    import time
    desc_str = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + " 清单模式"

    text(desc_str)

    touch(Template(r"tpl1554461306175.png", record_pos=(0.417, -0.883), resolution=(1080, 2244)))

    #选择检查部位（使用poco优化）目前都是选择固定部位
    touch(Template(r"tpl1554461334642.png", record_pos=(-0.319, 0.526), resolution=(1080, 2244)))
    sleep(1)
    
    
    import random
    from poco.drivers.android.uiautomation import AndroidUiautomationPoco
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    

    #选择检查部位的页面
    while poco(desc="搜索"):
        check_area = poco("cn.smartinspection.combine:id/a00").offspring("cn.smartinspection.combine:id/a5z")   
        poco(text=check_area[random.randint(0,len(check_area)-1)].get_text()).click()
        #判断有无图纸位置，有则证明已完成部位选择，点击后还有证明部位没有图纸    
        #存在检查部位没有图纸的可能,则应重新点击检查部位组件，再选择部位
        sleep(1)
        if poco(text="图纸位置"):
            poco(text="图纸位置").click()
            sleep(3)
        if poco(text="图纸位置"):
            touch(Template(r"tpl1554461334642.png", record_pos=(-0.319, 0.526), resolution=(1080, 2244)))

            continue

    #上一步已完成图纸的选择
    touch(Template(r"tpl1554462939849.png", record_pos=(0.23, -0.744), resolution=(1080, 2244)))

    

    sleep(1)
    pinch(in_or_out='out',center=(500,1300),percent=0.003)
    for i in range(3):
        x = random.randint(20,1500)
        y = random.randint(500,2000)
        touch((x,y))
        sleep(1)

    touch(Template(r"tpl1554463039626.png", record_pos=(0.437, -0.885), resolution=(1080, 2244)))

    swipe((500,1500),(500,700),duration=1) #从上到下画横线1秒

    touch(Template(r"tpl1554463187952.png", record_pos=(-0.304, 0.551), resolution=(1080, 2244)))
    touch(Template(r"tpl1554463207045.png", record_pos=(-0.241, -0.649), resolution=(1080, 2244)))
    sleep(1)
    touch(Template(r"tpl1554463236769.png", record_pos=(-0.283, 0.714), resolution=(1080, 2244)))
    touch(Template(r"tpl1554463247751.png", record_pos=(-0.33, -0.434), resolution=(1080, 2244)))
    touch(Template(r"tpl1554463254702.png", record_pos=(-0.333, -0.328), resolution=(1080, 2244)))

    touch(Template(r"tpl1554463273845.png", record_pos=(-0.413, -0.885), resolution=(1080, 2244)))
    sleep(1)

    #选择整改日期

    touch(Template(r"tpl1554463309693.png", record_pos=(-0.315, 0.904), resolution=(1080, 2244)))

    while exists(Template(r"tpl1554720329826.png", record_pos=(-0.343, 0.672), resolution=(1080, 2244))): #如果存在清空期限按钮证明未选中时间，向上滑动日历
        
        swipe((500,1500),(500,700),duration=1) #从下到上画横线1秒
        touch(Template(r"tpl1554463526291.png", record_pos=(-0.114, 0.309), resolution=(1080, 2244)))
        sleep(1)
    touch(Template(r"tpl1554463711646.png", record_pos=(0.435, -0.878), resolution=(1080, 2244)))
    
    

#清单模式页面下指派问题
def appoint_issue():
    touch(Template(r"tpl1554465417529.png", record_pos=(-0.243, 0.97), resolution=(1080, 2244)))
    swipe((500,1500),(500,700),duration=1) #从下到上画横线1秒
    swipe((500,1500),(500,700),duration=1) #从下到上画横线1秒
    
    
    while exists(Template(r"tpl1555324773798.png", record_pos=(-0.408, -0.011), resolution=(1080, 2244))):
        touch(Template(r"tpl1555324796176.png", record_pos=(-0.41, -0.015), resolution=(1080, 2244)))


    touch(Template(r"tpl1554465626999.png", record_pos=(0.134, 0.969), resolution=(1080, 2244)))
    touch(Template(r"tpl1554465654755.png", record_pos=(-0.328, -0.111), resolution=(1080, 2244)))
    touch(Template(r"tpl1554465670804.png", record_pos=(0.328, 0.162), resolution=(1080, 2244)))
    touch(Template(r"tpl1554465417529.png", record_pos=(-0.243, 0.97), resolution=(1080, 2244)))
    touch(Template(r"tpl1554465560338.png", record_pos=(-0.407, -0.191), resolution=(1080, 2244)))
    touch(Template(r"tpl1554465572674.png", record_pos=(-0.409, 0.164), resolution=(1080, 2244)))
    touch(Template(r"tpl1554465779618.png", record_pos=(0.378, 0.969), resolution=(1080, 2244)))
    while exists(Template(r"tpl1554463616188.png", record_pos=(-0.298, 0.675), resolution=(1080, 2244))): #如果存在清空期限按钮证明未选中时间，向上滑动日历
        swipe((500,1500),(500,700),duration=1) #从上到下画横线1秒
        touch(Template(r"tpl1554465844026.png", record_pos=(-0.001, 0.306), resolution=(1080, 2244)))
        sleep(1)
        touch(Template(r"tpl1554465985274.png", record_pos=(0.317, 0.16), resolution=(1080, 2244)))
        sleep(2)

        
#图纸模式指派问题
def photo_add_issue():
    
#from poco.drivers.android.uiautomation import AndroidUiautomationPoco
#poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    tuzhi = poco(text="图纸模式")
    tuzhi.click()

    if exists(Template(r"tpl1554701332898.png", record_pos=(-0.002, 0.596), resolution=(1080, 2244))):
        touch(Template(r"tpl1554701345132.png", record_pos=(0.002, 0.585), resolution=(1080, 2244)))
        sleep(1)

    quyu = poco("cn.smartinspection.combine:id/a7g")
    quyu.click()

    #4#第2层poco(text="4#")
    poco(text="4#").click()
    poco(text="第2层").click()

    pinch(in_or_out='out',center=(500,1300),percent=0.003)

    
    while exists(Template(r"tpl1554782207104.png", record_pos=(0.024, -0.765), resolution=(1080, 2244))):  #如果该UI存在则代表点中已存在的问题，需重新点击图纸
        x = random.randint(20,1000)
        y = random.randint(1000,1500)
        touch((x,y))
        sleep(1) #点击完后，页面并不会马上切换，仍可能检测到原页面造成继续点击，所以此处停留一秒

    touch(Template(r"tpl1554454352019.png", record_pos=(-0.35, -0.419), resolution=(1080, 2244)))

    wait(Template(r"tpl1554702440180.png", record_pos=(-0.002, 0.81), resolution=(1080, 2244)))
    sleep(1)


    touch(Template(r"tpl1554454378918.png", record_pos=(0.005, 0.81), resolution=(1080, 2244)))

    sleep(2)

    swipe((200,1000),(1000,1000),duration=1) #从左到右画横线1秒
    sleep(1)
    swipe((500,700),(500,1500),duration=1) #从上到下画横线1秒

    touch(Template(r"tpl1554454924528.png", record_pos=(0.43, -0.878), resolution=(1080, 2244)))

    touch(Template(r"tpl1554791311025.png", record_pos=(-0.42, -0.231), resolution=(1080, 2244)))

    #选择检查项，目前都是选择固定检查项（此处使用poco可做优化改为随机选择）

    touch(Template(r"tpl1554461013129.png", record_pos=(-0.228, -0.728), resolution=(1080, 2244)))  #此处有问题，可能会直接穿透到叶子节点

    touch(Template(r"tpl1554791537083.png", record_pos=(-0.261, -0.454), resolution=(1080, 2244)))

    touch(Template(r"tpl1554461212564.png", record_pos=(-0.298, 0.092), resolution=(1080, 2244)))

    sleep(5)

    touch(Template(r"tpl1554461236054.png", record_pos=(0.003, -0.055), resolution=(1080, 2244)))
    touch(Template(r"tpl1554461254955.png", record_pos=(0.031, 0.294), resolution=(1080, 2244)))

    text("这是一次自动图纸新增问题过程")
    touch(Template(r"tpl1554461306175.png", record_pos=(0.417, -0.883), resolution=(1080, 2244)))


    touch(Template(r"tpl1554791643020.png", record_pos=(0.443, -0.887), resolution=(1080, 2244)))







        
#
#if __name__ == '__main__':
    


#点亮屏幕          
shell('input keyevent 224')

#上划屏幕解锁
swipe((500,1500),(500,700),duration=0.1) #从下到上画横线1秒

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
    
enter_gcjc()
    
list_add_issue()
    
appoint_issue()


photo_add_issue()

#相关api 
#http://airtest.netease.com/docs/docs_AirtestIDE-zh_CN/5_airtest_framework/airtest_all_module/airtest.core.android.android.html

#shell('ls')
#clear_app("cn.smartinspection.combine")
          
#wake()



shell("input keyevent 223")





























