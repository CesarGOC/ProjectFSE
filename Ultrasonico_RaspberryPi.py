import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
class HCSR04:
	def __init__(self, Trig, Echo):
		self._T = Trig
		self._E = Echo
		GPIO.setup(self._T, GPIO.OUT, initial = 0)
		GPIO.setup(self._E, GPIO.IN)
	def _timing(self):
		GPIO.output(self._T, 1)
		time.sleep(0.00001)
		GPIO.output(self._T, 0)
		while GPIO.input(self._E)==0:
			pulse_start_time = time.time()
		while GPIO.input(self._E)==1:
			pulse_end_time = time.time()
		duration = pulse_end_time - pulse_start_time
		return duration
	def distance(self):
		duration = self._timing()
		cm = ((duration * 34300) / 2) - 2
		return cm
