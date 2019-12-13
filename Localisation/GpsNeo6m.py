import serial
import string
import pynmea2

<<<<<<< HEAD:GpsNeo6m.py
while True:
    port="/dev/ttyAMA0"
    ser = serial.Serial(port, 9600, timeout=0.5)
    dataout = pynmea2.NMEAStreamReader()
    newdata = ser.readline()
=======
	latitude = msg.lat
	longitude = msg.lon
	altitude = msg.altitude 
>>>>>>> 26b13797b22bae44fdfaa5bdbfb8d005f735b744:Localisation/GpsNeo6m.py
    
   # if newdata[0:6] == "$GPRMC":

    if newdata.find('GGA')>0: 
        newmsg=pynmea2.parse(newdata)
        lat = newmsg.latitude
        lng = newmsg.longitude
        alt = newmsg.altitude
        
        gps = "Latitude=" + str(lat) + "and Longitude=" + str(lng)+"Altitude" + str(alt)
        print(gps)
