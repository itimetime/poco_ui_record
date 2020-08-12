# -*- coding: utf-8 -*-
# @Time : 2020/8/10 10:01
# @Author : ck
# @FileName: loaddata.py
import json
from config.config import jsonCasePath
def loadData():
    with open(jsonCasePath,"r+",encoding="utf-8") as f:

        return json.loads(f.read())


