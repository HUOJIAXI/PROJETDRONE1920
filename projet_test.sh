#!/bin/bash

echo -n "Veuillez saisir le maxi nombre d'executions: "
read num
echo -n "L'intervalle entre les executions: "
read temp
echo -n "Veuillez saisir l'altitude a laquelle commencer les tests: "
read hgt

int=0

while true;
do
	cd /home/pi/projetdronetech/Localisation/
	alt=`python -c 'import GpsNeo6m; print GpsNeo6m.get()'`
	echo "L'altitude actuelle : $alt"
	if [ $alt -gt $hgt ]
	then
		python /home/pi/projetdronetech/TraitementDImage/Local_traite_V2.py
		sleep 0.1
		python /home/pi/projetdronetech/Pollutiondair/aqi_single.py.1
		sleep 0.1
		python /home/pi/projetdronetech/TSL2561/Python/lumiere.py 
		sleep 0.1
		python /home/pi/projetdronetech/Adafruit_AMG88xx_python/examples/pixels_test.py
		sleep 0.1
		let "int=int+1"
		echo "$int fois"
	
		sleep $temp
	
		if [ $int -eq $num ]
		then
			exit 0
		fi
	fi
done
	
