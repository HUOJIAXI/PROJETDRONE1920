#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from __future__ import division
import cv2
import numpy as np
#import matplotlib.pyplot as plt
from PIL import Image
import sys
import datetime
from time import sleep
import MySQLdb
 
src = cv2.imread('/home/pi/projetdronetech/TraitementDImage/Couvervegetal.jpg')
#print (ret)
#cv2.imwrite("./photo.png", src)
#cv2.imshow('src', src) 
cv2.imwrite('Couvervegetal.jpg', src)
 
fsrc = np.array(src, dtype=np.float32) / 255.0
(b,g,r) = cv2.split(fsrc)
gray = 2 * g - b - r
 
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)

gray_u8 = np.array((gray - minVal) / (maxVal - minVal) * 255, dtype=np.uint8)
(thresh, bin_img) = cv2.threshold(gray_u8, -1.0, 255, cv2.THRESH_OTSU)
#cv2.imshow('bin_img', bin_img)
 
#hist = cv2.calcHist([gray], [0], None, [256], [minVal, maxVal])
#plt.plot(hist)
#plt.show()

# gray_u8 = np.array((gray - minVal) / (maxVal - minVal) * 255, dtype=np.uint8)
# (thresh, bin_img) = cv2.threshold(gray_u8, -1.0, 255, cv2.THRESH_OTSU)
# cv2.imshow('bin_img', bin_img)
#image=cv2.cvtColor(bin_img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(bin_img,(5,5),0) 
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) 
#cv2.imshow('image', th3)
cv2.imwrite('Couvervegetal_bin.jpg', th3)

  # a = cv2.waitKey(0)
  # print a
area = 0

height, width = th3.shape
for i in range(height):
	for j in range(width):
		if th3[i, j] == 255:
			area += 1

#print(height*width)

#print(np.round(area/(height*width),3))

print('Couverture végétale:', np.round(area/(height*width)*100, 3),'%') 

m = np.round(area/(height*width)*100, 3)

#print('Couverture végétale:', area/(height*width)*100,'%') 

conn = MySQLdb.connect(
host = '127.0.0.1',
port = 3306,
user = 'pi',
passwd = 'projet2019',
db = 'PROJETDRONE'
)

#    conn = MySQLdb.connect(
#    host = 'localhost',
#    port = 3306,
#    user = 'root',
#    passwd = '',
#    db = 'PROJETDRONE'
#    )

cur = conn.cursor()
cur.execute("insert into COUVERTVEGETAL values ('%f', now())" % (m))
cur.close()
conn.commit()
conn.close()
 
#cv2.waitKey()
