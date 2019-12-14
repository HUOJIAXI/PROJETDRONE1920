# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# TSL2561
# This code is designed to work with the TSL2561_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Light?sku=TSL2561_I2CS#tabs-0-product_tabset-2

import smbus
import time
import MySQLdb
#import numpy as np 
import sys
import datetime
import serial
import pynmea2

# Get I2C bus
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
	    
bus = smbus.SMBus(1)

# TSL2561 address, 0x39(57)
# Select control register, 0x00(00) with command register, 0x80(128)
#		0x03(03)	Power ON mode

bus.write_byte_data(0x39, 0x00 | 0x80, 0x03)
# TSL2561 address, 0x39(57)
# Select timing register, 0x01(01) with command register, 0x80(128)
#		0x02(02)	Nominal integration time = 402ms
bus.write_byte_data(0x39, 0x01 | 0x80, 0x02)

time.sleep(0.5)

# Read data back from 0x0C(12) with command register, 0x80(128), 2 bytes
# ch0 LSB, ch0 MSB

lat,lon,alt = localisation()

data = bus.read_i2c_block_data(0x39, 0x0C | 0x80, 2)

# Read data back from 0x0E(14) with command register, 0x80(128), 2 bytes
# ch1 LSB, ch1 MSB
data1 = bus.read_i2c_block_data(0x39, 0x0E | 0x80, 2)

# Convert the data

ch0 = data[1] * 256 + data[0]
ch1 = data1[1] * 256 + data1[0]

# Stock the data
conn = MySQLdb.connect(
host = '127.0.0.1',
port = 3306,
user = 'pi',
passwd = 'projet2019',
db = 'PROJETDRONE'
)

cur = conn.cursor()
cur.execute("insert into LUMINEUSE values ('%d', '%d', '%d','%f','%f','%f', now())" % (ch0,ch1,(ch0 - ch1),lat,lon,alt))
cur.close()
conn.commit()
conn.close()

# Output data to screen
print "Full Spectrum(IR + Visible) :%d lux" %ch0
print "Infrared Value :%d lux" %ch1
print "Visible Value :%d lux" %(ch0 - ch1)

