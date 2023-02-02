"""
@Description :   py脚本名字一定要写成 tasks.py
                 invoke是一个管理任务和shell的工具框架
                 安装方式: pip install invoke
                 常用命令: 在terminal 中 cd 到tasks.py的上一级路径, 然后invoke --list 或者invoke -l 
                 调用方式: 同样的teminal路径下, invoke hello 或者 invoke greet China
@Author      :   jerry 
@Time        :   2023/02/02 11:43:23
"""

from invoke import task

@task
def hello(c):
    print("Hello world!")

@task(help={'name': 'A param for test'})
def greet(c, name):
    c.run(f"echo {name}加油!")
