   import serial
   import string
   import pynmea2
   
   def get():
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
  
              gps = "Latitude=" + str(lat) + "and Longitude=" + str(lng)+"Altitude" + str(alt)
              return gps

if __name__="__main__":
	gps=get()
	print(gps)

