# Traitement d'image
## Les images prises par la capteur de caméra sur le drone devraient être traitées en vue de trouver le pourcentage de couvert végétal.

Editeur:HUO JIAXI

## 3 versions pour augmenter la précision
1. image.py : Régler le seuil manuellement, pas précis
2. image_split.py : détecter mieux la couverture végétale que image.py
3. Local_trait_V2.py : La reglage du seuil est automatique et précise, grâce au nouveau algorithme

## Algorithme

> Extraire la partie verte

*  
        def green_style_v2(image):
            img=image[:,:,1]/(image[:,:,1]+image[:,:,2]+image[:,:,0]) # Détecter le pourcentage de la couleur vert(tous les types de vert: vert foncé, vert clair...), extraire la verte partie d'image(image[:,:,1] de la verte partie est supérieur que image[:,:,0] et image[:,:,2])

            img = cv2.GaussianBlur(img,(5,5),0) # Diminution de bruit 
            cv2.imshow('green', img)
            cv2.waitKey()
            return img

*       
        def man_seuillage(image,thresh=0.4)：# Réglage du seuil manuelle
            dst = (image >= thresh) * 1.0
            cv2.imshow('man_seuil', dst)
            cv2.waitKey()
            return dst
   

*
        def auto_seuillage(image,auto_seuil=0.38):  
            thresh = max(filters.threshold_otsu(image),auto_seuil)  # Réglage du seuil automatique et évider la possibilté d'écart de mesure lors de la détection d'images sans vert

            dst = (image >= thresh) * 1.0
            cv2.imshow('auto_seuil', dst)
            cv2.waitKey()
            return dst
