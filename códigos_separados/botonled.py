#
##author: Guadarrama Ortega César Alejandro
#
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
push =13
led = 15
GPIO.setup(led,GPIO.OUT)
GPIO.setup(push,GPIO.IN)

estadoLed = 0
estadoAnterior=0 
while True:
	
	led_push = GPIO.input(push)
	if (not led_push)==1 and estadoAnterior==0:
		estadoLed = 1 - estadoLed
		time.sleep(0.01)
	estadoAnterior = not led_push
	if estadoLed==1:
		GPIO.output(led,1)
	else:
		GPIO.output(led,0)

