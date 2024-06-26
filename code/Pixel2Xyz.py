import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2
import csv
import pandas


W=1024
H=512
yaw=512
x=0
y=0
c=135

def hori_d(h,H,d):
    if h > H/2:
        angle=(180/H) * (h - (H / 2))
        angle_hudu= math.radians(angle)
        d=d*math.cos(angle_hudu)
    else:
        angle=(180 / 512) * ((H / 2)-h)
        angle_hudu= math.radians(angle)
        d=d*math.cos(angle_hudu)
    return d


def pixel2Xyz(w,h,W,H,yaw,c,d,x,y):
    x_angle=(w-yaw)*(360/W)+c
    x_angle_hudu=math.radians(x_angle)
    #计算
    if h>(H/2):
        z_angle=(h-(H/2))*(180/H)
        z_angle_hudu=math.radians(z_angle)
        z_pixel=-math.tan(z_angle_hudu)*d
    else:
        z_angle=((H/2)-h)*(180/H)
        z_angle_hudu=math.radians(z_angle)
        z_pixel = d * math.tan(z_angle_hudu)

    x_pixel=x+d*math.sin(x_angle_hudu)
    y_pixel=y+d*math.cos(x_angle_hudu)
    return x_pixel,y_pixel,z_pixel


# w,h: the coordinates of the pixels in the SVP
# x,y: the geographical coordinates (in meters) of the SVP in the geographical space.
# W,H: the width and height of the SVP
# yaw: the column number in the vehicle’s heading direction within the SVP.
# c: the yaw angle of the SVP
# d: the projection distance of the 3D camera coordinates
x_pixel,y_pixel,z_pixel=pixel2Xyz(w,h,W,H,yaw,c,d,x,y)

