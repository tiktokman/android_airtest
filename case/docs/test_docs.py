# -*- encoding=utf8 -*-
__author__ = "zijie"
__title__ = "安卓端图纸文档模块回归测试报告"
__DESC__ = """
回归测试内容：
1.
2.
3.
"""


from airtest.core.api import *
import threading
import time
import random
import traceback
import os
import sys
import pytest
from airtest.report.report import simple_report


#导入上一层公共模块方法
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from login.login import *
from common_api.common_api import *

#导入最上级设置
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
from init_setting import *


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

@pytest.fixture(scope="module",autouse=True)
def env_init():
    auto_setup(__file__, logdir=docs_logdir, devices=["Android:///"])
    #auto_setup(__file__, logdir=docs_logdir, devices=["Android://127.0.0.1:5037/127.0.0.1:62001"])
    print("完成环境初始化")
    clear_app(apk)

    start_app(apk)
    sleep(2)
    
    authApp()

    login('kentest50','12345678','p1','kentest50')
    
    #selectMode("组织架构聚合")
    selectOrg_0(org_name='公司1项目贰')
    selectApp("图纸文档")    

    yield
    simple_report(filepath=os.path.realpath(__file__), logpath=docs_logdir, logfile=logfile, output=docs_output)
    print("输出文档模块报告")

#下拉更新文件列表
def update_list():
    while exists(Template(r"tpl1604241487554.png", record_pos=(0.006, -0.048), resolution=(1080, 2340))) or exists(Template(r"tpl1604241544411.png", threshold=0.8, record_pos=(0.003, -0.824), resolution=(1080, 2340))):
        swipe((500,700),(500,1500))
        sleep(5)
    

#选择tab
def select_tab(tab_name):
    #tab_name: 图纸、模型、文档、更多
    wait(Template(r"tpl1601118080311.png", record_pos=(-0.003, 0.884), resolution=(1080, 2340)))
    poco(text=tab_name).click()
    
#搜索文件并打开查看，返回
def select_file(filename):

    poco.wait_for_any(poco(type="androidx.recyclerview.widget.RecyclerView"))#等待文件列表
    
    touch(Template(r"tpl1603002812358.png", record_pos=(-0.415, -0.787), resolution=(1080, 2340)))
    text(filename)
    poco.wait_for_any(poco(text=filename,type='android.widget.TextView'))
#选择排序方式
def select_order(order):
    #更新时间：新->旧   更新时间：旧->新   文件名：A->Z  文件名：Z->A
    touch(Template(r"tpl1603006395723.png", record_pos=(0.433, -0.8), resolution=(1080, 2340)))
    poco.wait_for_any(poco(text="选择排序方式"))
    sleep(1)
    poco(text=order).click()
    


    

#用例

#查看图纸
def draw():
    try:
        select_tab("图纸")
        update_list()
        select_file("1")
        assert_exists(Template(r"tpl1603004574808.png", record_pos=(-0.381, -0.254), resolution=(1080, 2340)), "找到图纸")
        poco(text="1",type='android.widget.TextView').click()
        poco.wait_for_all(poco(text='拖动'))
        pinch(in_or_out='out',center=(500,1300),percent=0.3)  #放大
        sleep(0.5)
        pinch(in_or_out='in',center=(500,1300),percent=0.5)   #缩小
        poco(name="转到上一层级").click()
        poco(text="取消").click()
    except:
        log("出错啦",traceback.format_exc())
def model():
    try:
        select_tab("模型")
        update_list()
        select_file("BIM示例")
        assert_exists(Template(r"tpl1603004840739.png", record_pos=(-0.324, -0.802), resolution=(1080, 2340)), "找到模型")

        poco(text="BIM示例",type='android.widget.TextView').click()
        wait(Template(r"tpl1603008453158.png", record_pos=(0.435, -0.69), resolution=(1080, 2340)), timeout=60)#网络拥挤或模型较大时加载较慢，等待时间延长
        sleep(1)
        pinch(in_or_out='out',center=(500,1300),percent=0.3)  #放大
        sleep(0.5)
        pinch(in_or_out='in',center=(500,1300),percent=0.5)   #缩小
        poco(name="转到上一层级").click()
        poco(text="取消").click()
    except:
        log("出错啦",traceback.format_exc())
    
def file_manage():
    try:
        select_tab("文档")
        update_list()
        swipe((500,800),(500,1200))
        sleep(2)
        select_file("55555")
        assert_exists(Template(r"tpl1603006009690.png", record_pos=(-0.356, -0.802), resolution=(1080, 2340)), "找到文档")
        poco(text="55555",type='android.widget.TextView').click()
        sleep(1)
        assert_exists(Template(r"tpl1603006137836.png", record_pos=(0.008, -0.017), resolution=(1080, 2340)), "打开文档")  
        pinch(in_or_out='out',center=(500,1300),percent=0.1)  #放大
        sleep(0.5)
        pinch(in_or_out='in',center=(500,1300),percent=0.5)   #缩小
        poco(name="转到上一层级").click()
        poco(text="取消").click()
    except:
        log("出错啦",traceback.format_exc())




@pytest.mark.docs
class TestDocs():


    #@pytest.mark.skip(reason='skip')
    def test_01_draw_manage(self):
        draw()
    #@pytest.mark.skip(reason='skip')
    def test_02_model_manage(self):
        model()
    def test_03_file_manage(self):
        file_manage()
    #@pytest.mark.skip(reason='skip')
    def test_04_order_manage(self):
        select_order(order="文件名：Z->A")
        sleep(1)
        poco(desc="转到上一层级").click()

        
if __name__ == '__main__':
    pytest.main(["-s","test_docs.py"])  
