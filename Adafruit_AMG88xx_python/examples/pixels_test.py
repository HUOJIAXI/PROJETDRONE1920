#!/usr/bin/python
# Copyright (c) 2017 Adafruit Industries
# Author: Dean Miller
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# Can enable debug output by uncommenting:
#import logging
#logging.basicConfig(level=logging.DEBUG)

from Adafruit_AMG88xx import Adafruit_AMG88xx
from time import sleep
import MySQLdb
#import numpy as np 
import sys
import datetime

# import Adafruit_AMG88xx.Adafruit_AMG88xx as AMG88

# Default constructor will pick a default I2C bus.
#
# For the Raspberry Pi this means you should hook up to the only exposed I2C bus
# from the main GPIO header and the library will figure out the bus number based
# on the Pi's revision.
#
# For the Beaglebone Black the library will assume bus 1 by default, which is
# exposed with SCL = P9_19 and SDA = P9_20.
sensor = Adafruit_AMG88xx()

# Optionally you can override the bus number:
#sensor = AMG88.Adafruit_AMG88xx(busnum=2)

#wait for it to boot
sleep(.1)

#while(1):
time_stamp = datetime.datetime.now()

indice = 0
a = sensor.readPixels()
while indice < len(a):
	if a[indice] == 0.0:
		a = sensor.readPixels()
		indice = 0
	else:
		indice = indice + 1

b = sum(a)/len(a)
#	b = np.array(a)
#	b = b - b.min()
#	init = b.tolist()
#	print(init)
fhandle = open('donnee2.txt', 'a+w');
stdo = sys.stdout
sys.stdout=fhandle
print time_stamp.strftime('%Y.%m.%d-%H:%M:%S')
print(a)
sys.stdout=stdo
fhandle.close()
#	print open('donnee2.txt').read()

conn = MySQLdb.connect(
host = '127.0.0.1',
port = 3306,
user = 'pi',
passwd = 'projet2019',
db = 'PROJETDRONE'
)

cur = conn.cursor()
cur.execute("insert into TEMPMUR values ('%f', now())" % (b))
cur.close()
conn.commit()
conn.close()
print time_stamp.strftime('%Y.%m.%d-%H:%M:%S')
print(a)
sleep(1)

