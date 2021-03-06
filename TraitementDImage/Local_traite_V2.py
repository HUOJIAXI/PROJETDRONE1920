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
	#cv2.imshow('color',img)
	#cv2.waitKey()
	return img+1/255

def green_style_v2(image):
	img=image[:,:,1]/(image[:,:,1]+image[:,:,2]+image[:,:,0])
	#img=(img-np.min(img))/(np.max(img)-np.min(img))
	#cv2.imwrite('traite.png',img)
	#cv2.imshow('green', img)
	#cv2.waitKey()
	return img

def man_seuillage(image,thresh=0.4):
    
    dst = (image >= thresh) * 1.0
    #cv2.imwrite('imagesessai.jpg',dst)
    #cv2.imshow('man_seuil', dst)
    #cv2.waitKey()
    return dst

def auto_seuillage(image,auto_seuil=0.38):
    thresh = max(filters.threshold_otsu(image),auto_seuil)
    dst = (image >= thresh) * 1.0
    # cv2.imshow('auto_seuil', dst)
    #cv2.imwrite('imagetraite.png',dst)
    # cv2.waitKey()
    return dst

def compter_pourcentage(image,area=0):
	image_origin=image*255;
	cv2.imwrite('imagetraite.png',image_origin)
	height, width = image.shape
	for i in range(height):
		for j in range(width):
			if image[i, j] == 1:
				area += 1
	print(area)
	pourcent = np.round(area/(height*width)*100, 3)
	return pourcent

def localisation():
    while True:
	port="/dev/ttyAMA0"
	ser = serial.Serial(port, 9600, timeout=0.5)
	dataout = pynmea2.NMEAStreamReader()
	newdata = ser.readline()
    
   # if newdata[0:6] == "$GPRMC":

	if newdata.find('GGA')>0: 
	    newmsg=pynmea2.parse(newdata)
	    lat = newmsg.latitude
	    lng = newmsg.longitude
	    alt = newmsg.altitude
	    return lat, lng, alt
	else:
	    continue

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
    m_img=man_seuillage(g_img)
    pourcent=compter_pourcentage(a_img)
    try:      
   	 lat,lon,alt = localisation()
    except pynmea2.nmea.ChecksumError:
   	 lat,lon,alt = localisation()
    stockage(pourcent,lat,lon,alt) 
    print('Couverture vegetale:', pourcent,'%','at the point:',lat, lon, alt) 
