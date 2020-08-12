# -*- coding: utf-8 -*-
# @Time : 2020/8/7 14:59
# @Author : ck
# @FileName: recorder.py
import json
import os

from pocouwa.execute import Execute_Poco
from .loaddata import loadData
from config.config import jsonCasePath


class Recorder:
    def __init__(self, name, poco):
        self.name = name
        self.jsonData = {
            "author": None,
            "gameName": name,
            "steps": [],
            "originPage": None,
            "executeTime": 0
        }

    def updata(self, key: str, value):
        self.jsonData[key] = value

    def addSteps(self, step: list):
        self.jsonData["steps"].extend(step)

    def savaData(self):
        casePath = os.path.join(jsonCasePath,self.name)
        with open(casePath, "w+", encoding="utf-8") as f:
            f.write(json.dumps(self.jsonData, indent=2))


class UserOperator(Recorder):
    allSteps = []

    def __init__(self, name, poco):
        super().__init__(name, poco)
        self.poco = poco
        self.executor = Execute_Poco(self.poco)

    def remind(self, node_list):
        index_list = input("请选择你要点击的节点:").split(' ')
        if '-' in index_list[0]:
            start, end = index_list[0].split("-")
            index_list = []
            for i in range(int(start), int(end) + 1):
                index_list.append(i)

        self.steps = [node_list[int(x)] for x in index_list]
        print("执行操作:")
        self.executor.execute_now(self.steps)

    def expect(self):
        answer = input("是否达到预期结果").upper()
        if answer == "Y":
            self.allSteps.extend(self.steps)
        elif answer == "END":
            self.allSteps.extend(self.steps)
            self.addSteps(self.allSteps)
            self.savaData()
        elif answer == "CODE":
            code = input("请输入要插入的code")
            self.steps[0]["code"] = code
            self.allSteps.extend(self.steps)
        elif answer == "F":
            self.steps[0]["sleep"] = 5
            self.allSteps.extend(self.steps)
            return False
        else:
            pass
        return True

    def executorData(self):
        data = loadData()
        self.executor.execute_data(data)


if __name__ == '__main__':
    a = UserOperator("test")
    # a.remind([])
