# Traitement d'image
## Les images prises par la capteur de caméra sur le drone devraient être traitées en vue de trouver le pourcentage de couvert végétal.

## 3 versions pour augmenter la précision

## Algorithme

> Extraire la partie verte

*  
        def green_style_v2(image):
            img=image[:,:,1]/(image[:,:,1]+image[:,:,2]+image[:,:,0])
            img=(img-np.min(img))/(np.max(img)-np.min(img))
            img = cv2.GaussianBlur(img,(5,5),0) 
            cv2.imshow('green', img)
            cv2.waitKey()
            return img

*       
        def man_seuillage(image,thresh=0.4)：
            dst = (image >= thresh) * 1.0
            cv2.imshow('man_seuil', dst)
            cv2.waitKey()
            return dst
   

*
        def auto_seuillage(image):  
            thresh = filters.threshold_otsu(image)
            dst = (image >= thresh) * 1.0
            cv2.imshow('auto_seuil', dst)
            cv2.waitKey()
            return dst
