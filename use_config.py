# -*- coding: utf-8 -*-

import configparser

config = configparser.ConfigParser()

config.read("config.ini", encoding="utf-8")

print(config.get("path", "logdir"))

print(config.get("path", "project_root"))



'''

[mysql]

name = admin

host = 255.255.255.0

proxy = 6037

password = 123456

pool = true

time = 3



import configparser

config = configparser.ConfigParser()

config.read("config.ini", encoding="utf-8")

config.sections()  # 获取section节点

config.options('mysql')  # 获取指定section 的options即该节点的所有键

config.get("mysql", "name")  # 获取指定section下的options

config.getint("mysql", "proxy")  # 将获取到值转换为int型

config.getboolean("mysql", "pool")  # 将获取到值转换为bool型

config.getfloat("mysql", "time")  # 将获取到值转换为浮点型

config.items("mysql")  # 获取section的所用配置信息

config.set("mysql", "name", "root")  # 修改db_port的值为69

config.has_section("mysql")  # 是否存在该section

config.has_option("mysql", "password")  # 是否存在该option

config.add_section("redis")  # 添加section节点

config.set("redis", "name", "redis_admin")  # 设置指定section 的options

config.remove_section("redis")  # 整个section下的所有内容都将删除

config.remove_option("mysql", 'time')  # 删除section下的指定options

config.write(open("Config", "w"))  # 保存config

'''
