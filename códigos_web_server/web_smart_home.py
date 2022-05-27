##web_smart_home.py
#autor: Guadarrama Ortega César Alejandro

import RPi.GPIO as GPIO
import time
import sys
import cv2
from Ultrasonico_RaspberryPi import HCSR04

#Pines para usar
led=15
push_yellow = 13
BUZZER_PIN = 12  # Buzzer
push_red=11
servo_uno = 3
ultra = HCSR04(5,7)


#estados de botón
estadoLed = 0
estadoAnterior=0 

#notas de timbre
notes = {  # Dict that contains the the first scale notes frequencies
    'C': 0.002109, 'D': 0.001879, 'E': 0.001674, 'F': 0.001580, 'G': 0.001408,
    'A': 0.001254, 'B': 0.001117, 'C1': 0.001054,
}

#Configuraciones
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(push_yellow,GPIO.IN)
GPIO.setup(push_red,GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(servo_uno, GPIO.OUT)

#variables servo
pulso = GPIO.PWM(servo_uno, 50)
pulso.start(2.5)

##Funciones PWM
pwm_led=GPIO.PWM(led,500)
pwm_led.start(100)


#Funciones de timbre
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
        cap = cv2.VideoCapture('cam2.mov')
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

#LEDS
def ledson(word):
	if word == "On":
		pwm_led.ChangeDutyCycle(100)

def ledsoff(word):
	if word == "Off":
		pwm_led.ChangeDutyCycle(0)
#Timbre
def timbre(word):
	if word == "On":
		print("se presiono timbre")
		for n in ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C1']:  # Play all notes
			play_sound(100, notes[n])
		cam(1)
#Garage
def garage(word):
	if word=="Automatic":
		aux=True
		while aux:
			time.sleep(1)
			distancia = ultra.distance()
			print("%.1f"%distancia)
			if distancia<5.5:
				for i in range(0,90):
					time.sleep(0.005)
					grados = (1.0/18.0)*(i)+2.5
					pulso.ChangeDutyCycle(grados)
				time.sleep(6)
				for i in range(90,0,-1):
					time.sleep(0.005)
					grados = (1.0/18.0)*(i)+2.5
					pulso.ChangeDutyCycle(grados)
				aux=False
					#sleep(6)
	if word=="Open":
		for i in range(0,90):
			time.sleep(0.005)
			grados = (1.0/18.0)*(i)+2.5
			pulso.ChangeDutyCycle(grados)
	if word=="Close":
		for i in range(90,0,-1):
			time.sleep(0.005)
			grados = (1.0/18.0)*(i)+2.5
			pulso.ChangeDutyCycle(grados)
#Cambiar iluminacion
def pwm(valor):
	duty_s=valor
	duty=int(duty_s)
	pwm_led.ChangeDutyCycle(duty)
	
def camara(numero):
    delay = 1/30 #tiempo de espera en cada frame
    #Seleccion de camaras
    if numero == "1":
        cap = cv2.VideoCapture('cam1.mov')
    if numero == "2":
        cap = cv2.VideoCapture('cam2.mov')
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

def bcd(valor):
	pass
	


