# -*- coding: utf-8 -*-
# @Time : 2020/8/6 17:30
# @Author : ck
# @FileName: tr.py

import os
import cv2
from multiprocessing import Process


class Cv_Operator():
    def mark(self, nodeList, imgPath):
        img = cv2.imread(imgPath)
        x, y = img.shape[0:2]
        if x>720:
            t = x/720
            img = cv2.resize(img, (int(y/t), int(x/t)))
            x, y = img.shape[0:2]
        # xmin = 100
        # xmax = 200
        # ymin = 100
        # ymax = 300
        # cv2.rectangle(img1, (xmin, ymin), (xmax, ymax), (0, 0, 255), 2)
        # cv2.rectangle(img1, (xmin, ymax), (xmax, ymin), (255, 0, 0), 2)
        # x, y = img.shape[0:2]
        points_list = []
        for node in nodeList:
            a, b = node["pos"]
            points_list.append((int(a * y), int(b * x)))
        point_size = 6
        point_color = (235, 0, 255)  # BGR
        thickness = 2  # 可以为 0 、4、8
        fontFace = cv2.FONT_HERSHEY_TRIPLEX
        fontScale = 0.5
        fontcolor = (0, 255, 0)  # BGR
        thickness_font = 1
        lineType = 10
        bottomLeftOrigin = 1
        for point in points_list:
            index = points_list.index(point)
            cv2.circle(img, point, point_size, point_color, thickness)
            cv2.putText(img, str(index), point, fontFace, fontScale, fontcolor, thickness_font, lineType)
            print(f"No.:{str(index):4} Name:{nodeList[index]['name']:20}", end='')
            if (index + 1) % 3 == 0:
                print("")
        print("")
        cv2.imshow('src', img)
        cv2.waitKey()
    def show_image(self):
        ...


if __name__ == '__main__':
    cv = Cv_Operator()
    cv.mark([],r"C:\Users\ck\PycharmProjects\poco_test\test\1.jpg")
    pass
