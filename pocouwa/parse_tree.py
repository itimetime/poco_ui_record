# -*- coding: utf-8 -*-
# @Time : 2020/7/28 11:02
# @Author : ck
# @FileName: autotest.py
import json
import random
import time

from poco.drivers.unity3d import UnityPoco




# 进行PocoUI树解析
class Poco_parse():
    def __init__(self):
        self.poco = UnityPoco()
    def get_poco(self):
        return self.poco
    # 获取pocoui树原数据
    def load_poco_tree(self):
        self.click_nodes = []
        ui_tree = self.poco.agent.hierarchy.dump()
        click_nodes = self.scan_tree(ui_tree["children"])
        return click_nodes

    # 递归解析
    def scan_tree(self, children):
        if isinstance(children, dict) is True:
            payload = children["payload"]
            if self.is_valid(payload):
                if "children" in children.keys():
                    # pass
                    del children["children"]
                # print(children["payload"]["pos"],",")
                # 处理相关数据
                tempNode = {"name":payload["name"],"pos":payload["pos"],"type":payload["type"]}
                self.click_nodes.append(tempNode)
                return
            if "children" in children.keys():
                self.scan_tree(children["children"])
            else:
                return
        elif isinstance(children, list) is True:
            for i in children:
                self.scan_tree(i)
        return self.click_nodes

    # 外部获取数据的接口
    def get_poco_tree(self):
        return self.load_poco_tree()

    # 判断是否为有效可点击结点
    def is_valid(self, payload):
        if payload["clickable"] is True:
            if 1 > payload["pos"][0] > 0 and 1 > payload["pos"][1] > 0:
                return True
        return False



