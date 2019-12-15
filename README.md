# PROJETDRONE1920

Les scripts concernant:
1. Capteur thermique: Adafruit_AMG8833_python
2. Capteur couvert végétale: Caméra 
3. Capteur pollution lumnineuse: TSL
4. Capteur pollution d'air: aqi.py.1
5. 2 scripts python pour détecter le pourcentage de couvert végétal sous le dossier TraitementDImage

image_split.py détecter mieux la couverture végétale que image.py.

Je préfère appliquer le image_split.py afin de détecter la couverture végétale...Le resultat de test: resultat_couvert_vegetale.png

Les données sont bien stockées dans la base de données...

Avant l'éxecution du script image.py, il convient de régler la valeur de RGB selon la situation réelle (La première image)

==============================================================================

Mise à jour le 15/12/2019

Editeur: HUOJIAXI

Les travaux de script shell étaient terminés. Grâce au scipt shell projet_test.sh, on pourra lancer les mesures automatiquement. Les mesures se commenceront automatiquement lors que le drone atteindra l'altitude prévue (On régle l'altitude de démarrage lors que l'on lance le shell)

Une fois une mesure est prise, la localisation actuelle va être stockée avec le resultat de mesure dans la base de donnée.

La mise en place de QGIS était terminée. Les données de mesures peuvent être prises sous le format txt de base de donnée.

https://github.com/HUOJIAXI/PROJETDRONE1920.git/raw/master/Exemple_QGIS.png 
