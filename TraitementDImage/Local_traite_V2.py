#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from __future__ import division
import cv2
from skimage import filters
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img_path='/Users/huojiaxi/Desktop/Unknown.jpeg'

def read_img(path=img_path):
	# img=cv2.imread(path).astype(np.float)/255
	cap = cv2.VideoCapture(0)
	ret, src = cap.read(0)
 	img=src.astype(np.float)/255
	img=cv2.resize(img,(480,320))
	cv2.imshow('color',img)
	cv2.waitKey()
	return img+1/255

def green_style_v2(image):
    img=image[:,:,1]/(image[:,:,1]+image[:,:,2]+image[:,:,0])
    img=(img-np.min(img))/(np.max(img)-np.min(img))
    cv2.imshow('green', img)
    cv2.waitKey()
    return img

def man_seuillage(image,thresh=0.4):
    dst = (image >= thresh) * 1.0
    cv2.imshow('man_seuil', dst)
    cv2.waitKey()
    return dst

def auto_seuillage(image):
	thresh = filters.threshold_otsu(image)
	dst = (image >= thresh) * 1.0
	cv2.imshow('auto_seuil', dst)
	cv2.waitKey()
	return dst

def compter_pourcentage(image,area=0):
	height, width = image.shape
	for i in range(height):
		for j in range(width):
			if image[i, j] == 1:
				area += 1
	print(area)
	pourcent = np.round(area/(height*width)*100, 3)
	return pourcent


if __name__=="__main__":
    img=read_img()
    g_img=green_style_v2(img)
    a_img=auto_seuillage(g_img)
    pourcent=compter_pourcentage(a_img)
    print('Couverture végétale:', pourcent,'%') 

 
# #src = cv2.imread('/Users/huojiaxi/Desktop/Unknown.jpeg')
# cap = cv2.VideoCapture(0)
# ret, src = cap.read(0)
# #print (ret)
# #cv2.imwrite("./photo.png", src)
# cv2.imshow('src', src) 
 
# fsrc = np.array(src, dtype=np.float32) / 255.0
# (b,g,r) = cv2.split(fsrc)
# gray = 2 * g - b - r
 
# (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)

# gray_u8 = np.array((gray - minVal) / (maxVal - minVal) * 255, dtype=np.uint8)
# (thresh, bin_img) = cv2.threshold(gray_u8, -1.0, 255, cv2.THRESH_OTSU)
# cv2.imshow('bin_img', bin_img)
 
# #hist = cv2.calcHist([gray], [0], None, [256], [minVal, maxVal])
# #plt.plot(hist)
# #plt.show()

# # gray_u8 = np.array((gray - minVal) / (maxVal - minVal) * 255, dtype=np.uint8)
# # (thresh, bin_img) = cv2.threshold(gray_u8, -1.0, 255, cv2.THRESH_OTSU)
# # cv2.imshow('bin_img', bin_img)
# #image=cv2.cvtColor(bin_img, cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(bin_img,(5,5),0) 
# ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) 
# cv2.imshow('image', th3)
#   # a = cv2.waitKey(0)
#   # print a
# area = 0

# area=sum(th3/255)
# height, width = th3.shape
# #for i in range(height):
# #	for j in range(width):
# #		if th3[i, j] == 255:
# #			area += 1

# #print(height*width)

# #print(np.round(area/(height*width),3))

# print('Couverture végétale:', np.round(area/(height*width)*100, 3),'%') 

# #print('Couverture végétale:', area/(height*width)*100,'%') 
 
# cv2.waitKey()