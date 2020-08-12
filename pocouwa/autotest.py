# -*- coding: utf-8 -*-
# @Time : 2020/7/28 11:02
# @Author : ck
# @FileName: autotest.py
import json
import random
import time

from poco.drivers.unity3d import UnityPoco

poco = UnityPoco()


# 进行PocoUI树解析
class Scan_poco_tree():
    # 统计页面可点击节点，并对可点击节点进行存储
    def __init__(self):
        self.n = 0
        self.has_click_nodes = []
        self.has_load_page = ["0"]
        self.click_nodes = []

    # 获取pocoui树原数据
    def load_poco_tree(self):
        self.click_nodes = []
        ui_tree = poco.agent.hierarchy.dump()
        return self.scan_tree(ui_tree["children"])

    # 递归解析
    def scan_tree(self, children):
        if isinstance(children, dict) is True:
            payload = children["payload"]
            if self.is_valid(payload):
                if "children" in children.keys():
                    # pass
                    del children["children"]
                print(children["payload"]["pos"],",")
                self.click_nodes.append(children)
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
    def show_number(self):
        print(self.n)
        return self.load_poco_tree()

    # 判断是否为有效可点击结点
    def is_valid(self, payload):
        if payload["clickable"] is True:
            if 1 > payload["pos"][0] > 0 and 1 > payload["pos"][1] > 0:
                self.n += 1
                return True
        return False

    def sava_page(self, click_nodes):
        page_name = ''
        for node in click_nodes:
            page_name += node["name"]
        if page_name == self.has_load_page[-1]:
            print("页面元素未进行变动")
            print(len(self.has_load_page))
            return True
        else:
            self.has_load_page.append(page_name)
            print(self.has_load_page)
            return False

    def start_explore(self):
        click_nodes = self.load_poco_tree()
        print(click_nodes)
        # self.sava_page(click_nodes)
        # self.start_click(click_nodes)


    def start_click(self, click_nodes):
        # for node in click_nodes:
        while click_nodes != []:
            node = random.choice(click_nodes)
            click_nodes.remove(node)
            print("点击", node["name"])
            if node["name"]+str(node["payload"]["_instanceId"]) in self.has_click_nodes or node["name"] == "BtnToggle":
                print("结点被点击过")
                if node["name"] == "btnClose":
                    poco.click(node["payload"]["pos"])
                continue
            else:
                poco.click(node["payload"]["pos"])
                self.has_click_nodes.append(node["name"]+str(node["payload"]["_instanceId"]))
            time.sleep(2)
            click_nodes = self.load_poco_tree()
            if self.sava_page(click_nodes):
                pass
            else:
                self.start_click(click_nodes)
        return


if __name__ == '__main__':
    # clicked_node_list = []
    scan = Scan_poco_tree()
    scan.start_explore()
    # scan.load_poco_tree()
    # click_nodes = scan.show_number()
    # # node = random.choice(click_nodes)
    # for node in click_nodes:
    #     print("点击", node["name"])
    #     pocouwa.click(node["payload"]["pos"])
    #     clicked_node_list.append(node["name"]+str(node["payload"]["pos"]))
    #     time.sleep(500)
    #
    #     print(clicked_node_list)
# adb shell screencap -p /sdcard/01.png
#     pocouwa.click([0.7279968, 0.166015625])


# TODO 已遍历节点更换为字典结构 记录已经遍历的结点信息 增加白名单
