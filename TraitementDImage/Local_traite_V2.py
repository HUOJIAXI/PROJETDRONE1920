#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from __future__ import division
import cv2
from skimage import filters
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import sys
import datetime
from time import sleep
import MySQLdb

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
	img = cv2.GaussianBlur(img,(5,5),0) 
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

def stockage(pourcent):
    conn = MySQLdb.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'pi',
    passwd = 'projet2019',
    db = 'PROJETDRONE'
    )
    
    cur = conn.cursor()
    cur.execute("insert into COUVERTVEGETAL values ('%f',now())" % (pourcent))
    cur.close()
    conn.commit()
    conn.close()

if __name__=="__main__":
    img=read_img()
    g_img=green_style_v2(img)
    a_img=auto_seuillage(g_img)
    pourcent=compter_pourcentage(a_img)
    stockage(pourcent)
    print('Couverture végétale:', pourcent,'%') 
