#
##author: Guadarrama Ortega César Alejandro
#
import RPi.GPIO as GPIO
import sys
import cv2
import time
#pip install opencv-python
#sudo apt-get install libatlas-base-dev
#pip install -U numpy 




BUZZER_PIN = 12  # Buzzer pin number
push =11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(push,GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

notes = {  # Dict that contains the the first scale notes frequencies
    'C': 0.002109, 'D': 0.001879, 'E': 0.001674, 'F': 0.001580, 'G': 0.001408,
    'A': 0.001254, 'B': 0.001117, 'C1': 0.001054,
}
def play_sound(duration, frequency):  # Play different frequencies
    for i in range(duration):
        GPIO.output(BUZZER_PIN, GPIO.HIGH)
        time.sleep(frequency)
        GPIO.output(BUZZER_PIN, GPIO.LOW)
        time.sleep(frequency)
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
	led_push = GPIO.input(push)
	if led_push == 0:
		print("se presiono timbre")
		for n in ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C1']:  # Play all notes
			play_sound(100, notes[n])
		cam(1)
