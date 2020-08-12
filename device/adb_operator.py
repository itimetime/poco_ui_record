# -*- coding: utf-8 -*-
# @Time : 2020/8/5 14:18
# @Author : ck
# @FileName: adb_operator.py


import os
import re
import time

from config.config import adbPath
from config.config import imgPath

class Device():
    def __init__(self):
        # self.proImg = os.getcwd() + "\\img\\"
        self.device = self.get_device()
    def get_device(self):
        a = os.popen("adb devices")
        device = re.findall("\d\w+", a.read())
        if device == []:
            raise Exception("please connect device!")
        else:
            os.system(f"adb shell mkdir /sdcard/Ascreenshot")
            return device[0]

    def get_screen(self):

        imgName = str(time.time())+'.png'
        os.system(f"{adbPath} -s {self.device} shell screencap -p /sdcard/Ascreenshot/{imgName}")
        os.system(f"{adbPath} -s {self.device} pull /sdcard/Ascreenshot/{imgName} {imgPath}")
        return os.path.join(imgPath,imgName)


if __name__ == '__main__':
    d =Device()
    d.get_screen()