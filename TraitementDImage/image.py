import numpy as np 
import cv2 

img = cv2.imread('/Users/huojiaxi/Desktop/googlelogo_color_272x92dp.png') 

vert = [45, 165, 65] # RGB de la couleur végétale, il est nécessaire de la régler lors que la première figure sera générée
diff = 20 
boundaries = [([vert[2]-diff, vert[1]-diff, vert[0]-diff], 
       [vert[2]+diff, vert[1]+diff, vert[0]+diff])] 
# Seuil

for (lower, upper) in boundaries: 
    lower = np.array(lower, dtype=np.uint8) 
    upper = np.array(upper, dtype=np.uint8) 
    mask = cv2.inRange(img, lower, upper) 
    output = cv2.bitwise_and(img, img, mask=mask) 

    ratio_vert = cv2.countNonZero(mask)/(img.size/3) 
    print('Vert pixel percentage:', np.round(ratio_vert*100, 2)) 

    #cv2.imshow("images", np.hstack([img, output])) 
    cv2.waitKey(0) 