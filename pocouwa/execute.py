# -*- coding: utf-8 -*-
# @Time : 2020/8/7 14:26
# @Author : ck
# @FileName: execute.py
import time

class Execute_Poco(object):
    def __init__(self,Poco):
        self.Poco = Poco
    def execute_now(self,node: list):
        for step in node:
            print(f"点击{step['name']}")
            self.Poco.click(step['pos'])
            if "sleep" in step.keys():
                time.sleep(step['sleep'])
            else:
                # 默认三秒
                time.sleep(3)
    def execute_data(self,data:dict):
        print(f"初始界面data{data['originPage']},请确认，用例将在5s后执行...")
        print(f"用例作者f{data['author']}")
        for step in data['steps']:
            print(f"点击{step['name']}")
            self.Poco.click(step['pos'])
            if "sleep" in step.keys():
                time.sleep(step['sleep'])
            if "code" in step.keys():
                eval(step["code"])
            else:
                # 默认三秒
                time.sleep(3)