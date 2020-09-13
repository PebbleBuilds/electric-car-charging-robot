# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 20:28:19 2020

@author: Grace Wu
"""
import cv2
import numpy as np
import imutils
import glob
import os
from pathlib import Path
from datetime import datetime

#parameters
imagepath = 'C:/Users/Grace Wu/m19/src/img/*.JPG'
resizedw = 500
resizedh = 375

def findcircle(imagepath):
    #import image
    list_of_files = glob.glob(imagepath) # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    image = cv2.imread(latest_file)
    #make picture smaller
    resized = imutils.resize(image, width=resizedw)
    #make colour filter
    hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
    lower_range = np.array([60,90,90])
    upper_range = np.array([120,320,120])
    mask = cv2.inRange(hsv,lower_range,upper_range)
    img = cv2.bitwise_and(resized, resized, mask=mask)
    cv2.imshow('Image1', mask)
    cv2.waitKey(0)
    final = resized.copy()
    #detect circles in the image 
    circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 0.5, 41, param1=70, param2=12 , minRadius=0,maxRadius=175)
    biggest = [0,0]
    index = 0
    #show all circles
    if circles is not None:
        for i in circles[0,:]:
            # draw the outer circle
            if i[2] > biggest[1]:
                biggest[1] = i[2]
                biggest[0] = index
            cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
            index += 1
        cv2.imshow("HoughCircles", img)
        cv2.waitKey()
    #show biggest circle
        cv2.circle(final,(circles[0,biggest[0]][0],circles[0,biggest[0]][1]),circles[0,biggest[0]][2],(0,255,0),2)
        cv2.imshow("HoughCircles", final)
        cv2.waitKey()
        cv2.destroyAllWindows()
        return circles[0,biggest[0]]
    else: 
        print("error!") 
        cv2.destroyAllWindows()

circle = findcircle(imagepath)
print(circle)

        
