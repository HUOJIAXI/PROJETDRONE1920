#!/bin/bash

python /home/pi/projetdronetech/TraitementDImage/Local_traite_V2.py > /dev/null 2>&1 &
python /home/pi/projetdronetech/Pollutiondair/aqi_single.py.1 > /dev/null 2>&1 &
python /home/pi/projetdronetech/TSL2561/Python/lumiere.py > /dev/null 2>&1 &
python /home/pi/projetdronetech/Adafruit_AMG88xx_python/examples/pixels_test.py > /dev/null 2>&1 &
