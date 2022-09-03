import cv2
import imutils #Libreria para reescalar una imagen manteniendo su relacion de aspecto
from funciones import funcion_recuadro
from funciones import funcion_centro

#captura = cv2.VideoCapture(0) # Se usa la webcam
captura = cv2.VideoCapture('videos/prueba.mp4') # Se lee un video

# Se inializa el contador y la imagen gris
gray_a = 0 #np.zeros((360,640), dtype=np.uint8)
i = 0

while(captura.isOpened()):
    ret, image = captura.read() # Se toma un frame del video
    if ret == True:
        # Se reescala la imagen a un ancho de 640 manteniendo la relacion de aspecto
        imagen = imutils.resize(image, width=640)

        # Se convierte el frame a escala de grises y se halla la diferencia
        gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        # Se halla la diferencia en valor absoluto
        dif = cv2.absdiff(gray,gray_a)
        
        # Se binariza la diferencia con un umbral de 20
        _, img_bin = cv2.threshold(dif, 20, 255, cv2.THRESH_BINARY)
        # Se aplica un filtro para borrar algunos puntos
        img_bin = cv2.medianBlur(img_bin, 5)
        #final = cv2.GaussianBlur(final, (3,3), 0)
        
        # Mediante funciones se halla el centro y se dibuja un recuadro
        h,w,x,y = funcion_centro(img_bin/255)
        imagen_final = funcion_recuadro(imagen,h,w,x,y)
        
        A = sum(sum(img_bin)) # Se halla el area (pixeles^2)
        if A>20000:
            print('hay movimiento')
        else:
            print('no hay movimiento')
        
        # Se actualiza la imagen gris anterior cada 2 frames
        if i%2 == 0:
            aux = gray_a
            gray_a = gray
        
        i+=1 # Se aumentaen 1 el contador
        
        # Se muestran los resultaods del procesamiento de imagenes
        cv2.imshow('Diferencia de Imagenes grises', dif)
        cv2.imshow('Diferencia Binarizada', img_bin)
        cv2.imshow('Video final', imagen)
        
        cv2.waitKey(60) # Delay para que el video no vaya muy rapido
        
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    else: break

captura.release()
cv2.destroyAllWindows()

