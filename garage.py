import RPi.GPIO as GPIO
from time import sleep
from Ultrasonico_RaspberryPi import HCSR04
GPIO.setmode(GPIO.BOARD)

servo_uno = 3
ultra = HCSR04(5,7)

GPIO.setup(servo_uno, GPIO.OUT)

pulso = GPIO.PWM(servo_uno, 50)
pulso.start(2.5)
try:
	while True:
		distancia = ultra.distance()
		print("%.1f"%distancia)
		sleep(1)
		if distancia<6.0:
			for i in range(0,90):
				sleep(0.005)
				grados = (1.0/18.0)*(i)+2.5
				pulso.ChangeDutyCycle(grados)
			sleep(2)
			for i in range(90,0,-1):
				sleep(0.005)
				grados = (1.0/18.0)*(i)+2.5
				pulso.ChangeDutyCycle(grados)
			sleep(2)
except KeyboardInterrupt:
	pulso.stop()
	GPIO.cleanup()

