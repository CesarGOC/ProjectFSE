import cv2
import time


def cam(camara):
    delay = 1/30 #tiempo de espera en cada frame
    #Seleccion de camaras
    if camara == 1:
        cap = cv2.VideoCapture('cam1.mov')
    if camara == 2:
        cap = cv2.VideoCapture('cam2.mp4')
    #ciclo while de reproducción
    while (cap.isOpened()):
        ret,im=cap.read()
        if ret==False:
            break
        cv2.imshow('Imagen',im)
        if cv2.waitKey(1) & 0xFF == 27:
            break
        time.sleep(delay)
    cap.release()
    cv2.destroyAllWindows()

while True:
    cam(int(input("Selecciona una camara 1 o 2, recordar stop=ESC: ")))
    print("Quieres salir S/N")
    scan=input()
    if scan=="S":
        break
    else:
        continue
        






