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
import serial
import pynmea2

img_path='/Users/huojiaxi/Desktop/IMG_3217.jpg'

def read_img(path=img_path):
	#img=cv2.imread(path).astype(np.float)/255
	cap = cv2.VideoCapture(0)
	ret, src = cap.read(0)
	cv2.imwrite('Couvervegetal.jpg', src)
 	img=src.astype(np.float)/255
	img=cv2.resize(img,(480,320))
	img = cv2.GaussianBlur(img,(11,11),0)
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

def localisation():
	serialPort = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)
	str = serialPort.readline()
	if str.find('GGA') > 0:
		msg = pynmea2.parse(str)

	latitude = msg.lat
	longitude = msg.lon
	altitude = msg.altitude 

	return latitude, longitude, altitude

def stockage(pourcent,lat,lon,alt):
    conn = MySQLdb.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'pi',
    passwd = 'projet2019',
    db = 'PROJETDRONE'
    )
    
    cur = conn.cursor()
    cur.execute("insert into COUVERTVEGETAL values ('%f','%f','%f','%f',now())" % (pourcent,lat,lon,alt))
    cur.close()
    conn.commit()
    conn.close()

if __name__=="__main__":
    img=read_img()
    g_img=green_style_v2(img)
    a_img=auto_seuillage(g_img)
    pourcent=compter_pourcentage(a_img)      
    lat,lon,alt = localisation()
    stockage(pourcent,lat,lon,alt) 
    print('Couverture végétale:', pourcent,'%','at the point:',lat, lon, alt) 
