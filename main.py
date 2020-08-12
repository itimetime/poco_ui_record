# -*- coding: utf-8 -*-
# @Time : 2020/8/7 10:02
# @Author : ck
# @FileName: main.py

import os,time

from device.adb_operator import Device
from cv.mark_node import Cv_Operator
from pocouwa import parse_tree
from record.recorder import UserOperator
from multiprocessing import Process

if __name__ == '__main__':
    device = Device()
    Dumper = parse_tree.Poco_parse()
    poco = Dumper.get_poco()
    operator = UserOperator("test2",poco)
    cv = Cv_Operator()
    imgName = device.get_screen()
    # operator.executorData()
    while True:
        poco_tree = Dumper.get_poco_tree()
        showImg1 = Process(target=cv.mark,args=(poco_tree,imgName))
        showImg1.start()
        time.sleep(2)
        operator.remind(poco_tree,)
        showImg1.terminate()
        imgName = device.get_screen()
        showImg2 = Process(target=cv.mark,args=([],imgName))
        showImg2.start()
        time.sleep(2)
        if not operator.expect():
            imgName = device.get_screen()
        showImg2.terminate()


