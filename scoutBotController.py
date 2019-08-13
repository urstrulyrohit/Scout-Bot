from flask import Flask
from flask import render_template,request
import time
import RPi.GPIO as GPIO
from lxml import html
import requests

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
Motor1A = 16
Motor1B = 18
Motor1E = 22
 
Motor2A = 23
Motor2B = 21
Motor2E = 19

Motor3A = 11
Motor3B = 13
Motor3E = 15
 
Motor4A = 33
Motor4B = 35
Motor4E = 37

GPIO_TRIGGER1 = 38
GPIO_ECHO1 = 40

GPIO_TRIGGER2 = 32
GPIO_ECHO2 = 36

servo = 3

GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
GPIO.setup(GPIO_ECHO1, GPIO.IN)
GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
GPIO.setup(GPIO_ECHO2, GPIO.IN)

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
 
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

GPIO.setup(Motor3A,GPIO.OUT)
GPIO.setup(Motor3B,GPIO.OUT)
GPIO.setup(Motor3E,GPIO.OUT)
 
GPIO.setup(Motor4A,GPIO.OUT)
GPIO.setup(Motor4B,GPIO.OUT)
GPIO.setup(Motor4E,GPIO.OUT)

GPIO.setup(servo,GPIO.OUT)
pwm = GPIO.PWM(servo,50)
pwm.start(0)

print("Done")
a = 1
angle=0

def distance1():
	# set Trigger to HIGH
	GPIO.output(GPIO_TRIGGER1, True)
 
	# set Trigger after 0.01ms to LOW
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER1, False)
 
	StartTime = time.time()
	StopTime = time.time()
 
	# save StartTime
	while GPIO.input(GPIO_ECHO1) == 0:
		StartTime = time.time()
 
	# save time of arrival
	while GPIO.input(GPIO_ECHO1) == 1:
		StopTime = time.time()
 
	# time difference between start and arrival
	TimeElapsed = StopTime - StartTime
	# multiply with the sonic speed (34300 cm/s)
	# and divide by 2, because there and back
	distance = (TimeElapsed * 34300) / 2
 
	return distance

def distance2():
	# set Trigger to HIGH
	GPIO.output(GPIO_TRIGGER2, True)
 
	# set Trigger after 0.01ms to LOW
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER2, False)
 
	StartTime = time.time()
	StopTime = time.time()
 
	# save StartTime
	while GPIO.input(GPIO_ECHO2) == 0:
		StartTime = time.time()
 
	# save time of arrival
	while GPIO.input(GPIO_ECHO2) == 1:
		StopTime = time.time()
 
	# time difference between start and arrival
	TimeElapsed = StopTime - StartTime
	# multiply with the sonic speed (34300 cm/s)
	# and divide by 2, because there and back
	distance = (TimeElapsed * 34300) / 2
 
	return distance
print("dist2")
def left_side():
	data1="LEFT"
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)
	 
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.HIGH)

	GPIO.output(Motor3A,GPIO.HIGH)
	GPIO.output(Motor3B,GPIO.LOW)
	GPIO.output(Motor3E,GPIO.HIGH)
	 
	GPIO.output(Motor4A,GPIO.LOW)
	GPIO.output(Motor4B,GPIO.LOW)
	GPIO.output(Motor4E,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(Motor1E,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.LOW)
	GPIO.output(Motor3E,GPIO.LOW)
	GPIO.output(Motor4E,GPIO.LOW)
	#-------------
	return True

def right_side():
	data1="RIGHT"
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)
	 
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.HIGH)

	GPIO.output(Motor3A,GPIO.LOW)
	GPIO.output(Motor3B,GPIO.LOW)
	GPIO.output(Motor3E,GPIO.HIGH)
	 
	GPIO.output(Motor4A,GPIO.HIGH)
	GPIO.output(Motor4B,GPIO.LOW)
	GPIO.output(Motor4E,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(Motor1E,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.LOW)
	GPIO.output(Motor3E,GPIO.LOW)
	GPIO.output(Motor4E,GPIO.LOW)
	return True


def forward():
	if(distance2()>20):
		data1="FORWARD"
		GPIO.output(Motor1A,GPIO.HIGH)
		GPIO.output(Motor1B,GPIO.LOW)
		GPIO.output(Motor1E,GPIO.HIGH)
		 
		GPIO.output(Motor2A,GPIO.HIGH)
		GPIO.output(Motor2B,GPIO.LOW)
		GPIO.output(Motor2E,GPIO.HIGH)

		GPIO.output(Motor3A,GPIO.HIGH)
		GPIO.output(Motor3B,GPIO.LOW)
		GPIO.output(Motor3E,GPIO.HIGH)
		 
		GPIO.output(Motor4A,GPIO.HIGH)
		GPIO.output(Motor4B,GPIO.LOW)
		GPIO.output(Motor4E,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(Motor1E,GPIO.LOW)
		GPIO.output(Motor2E,GPIO.LOW)
		GPIO.output(Motor3E,GPIO.LOW)
		GPIO.output(Motor4E,GPIO.LOW)
		return True
	else:
		print("obstacle detected")
	return True

def reverse():
	if(distance1()>20):
		data1="REVERSE"
		GPIO.output(Motor1A,GPIO.LOW)
		GPIO.output(Motor1B,GPIO.HIGH)
		GPIO.output(Motor1E,GPIO.HIGH)
		 
		GPIO.output(Motor2A,GPIO.LOW)
		GPIO.output(Motor2B,GPIO.HIGH)
		GPIO.output(Motor2E,GPIO.HIGH)

		GPIO.output(Motor3A,GPIO.LOW)
		GPIO.output(Motor3B,GPIO.HIGH)
		GPIO.output(Motor3E,GPIO.HIGH)
		 
		GPIO.output(Motor4A,GPIO.LOW)
		GPIO.output(Motor4B,GPIO.HIGH)
		GPIO.output(Motor4E,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(Motor1E,GPIO.LOW)
		GPIO.output(Motor2E,GPIO.LOW)
		GPIO.output(Motor3E,GPIO.LOW)
		GPIO.output(Motor4E,GPIO.LOW)
	else:
		print("obstacle detected")
	return True

#------------------------------------------

def left_side_1():
	data1="LEFT"
	GPIO.output(Motor1A,GPIO.LOW)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)
	 
	GPIO.output(Motor2A,GPIO.HIGH)
	GPIO.output(Motor2B,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.HIGH)

	GPIO.output(Motor3A,GPIO.HIGH)
	GPIO.output(Motor3B,GPIO.LOW)
	GPIO.output(Motor3E,GPIO.HIGH)
	 
	GPIO.output(Motor4A,GPIO.LOW)
	GPIO.output(Motor4B,GPIO.LOW)
	GPIO.output(Motor4E,GPIO.HIGH)
	return True


def right_side_1():
	data1="RIGHT"
	GPIO.output(Motor1A,GPIO.HIGH)
	GPIO.output(Motor1B,GPIO.LOW)
	GPIO.output(Motor1E,GPIO.HIGH)
	 
	GPIO.output(Motor2A,GPIO.LOW)
	GPIO.output(Motor2B,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.HIGH)

	GPIO.output(Motor3A,GPIO.LOW)
	GPIO.output(Motor3B,GPIO.LOW)
	GPIO.output(Motor3E,GPIO.HIGH)
	 
	GPIO.output(Motor4A,GPIO.HIGH)
	GPIO.output(Motor4B,GPIO.LOW)
	GPIO.output(Motor4E,GPIO.HIGH)
	return True


def forward_1():
	if(distance2()>20):
		data1="FORWARD"
		GPIO.output(Motor1A,GPIO.HIGH)
		GPIO.output(Motor1B,GPIO.LOW)
		GPIO.output(Motor1E,GPIO.HIGH)
	 
		GPIO.output(Motor2A,GPIO.HIGH)
		GPIO.output(Motor2B,GPIO.LOW)
		GPIO.output(Motor2E,GPIO.HIGH)

		GPIO.output(Motor3A,GPIO.HIGH)
		GPIO.output(Motor3B,GPIO.LOW)
		GPIO.output(Motor3E,GPIO.HIGH)
	 
		GPIO.output(Motor4A,GPIO.HIGH)
		GPIO.output(Motor4B,GPIO.LOW)
		GPIO.output(Motor4E,GPIO.HIGH)
	return True


def reverse_1():
	if(distance1()>20):
		data1="REVERSE"
		GPIO.output(Motor1A,GPIO.LOW)
		GPIO.output(Motor1B,GPIO.HIGH)
		GPIO.output(Motor1E,GPIO.HIGH)
	 
		GPIO.output(Motor2A,GPIO.LOW)
		GPIO.output(Motor2B,GPIO.HIGH)
		GPIO.output(Motor2E,GPIO.HIGH)

		GPIO.output(Motor3A,GPIO.LOW)
		GPIO.output(Motor3B,GPIO.HIGH)
		GPIO.output(Motor3E,GPIO.HIGH)
	 
		GPIO.output(Motor4A,GPIO.LOW)
		GPIO.output(Motor4B,GPIO.HIGH)
		GPIO.output(Motor4E,GPIO.HIGH)
	return True

def stop():
	data1="STOP"
	GPIO.output(Motor1E,GPIO.LOW)
	GPIO.output(Motor2E,GPIO.LOW)
	GPIO.output(Motor3E,GPIO.LOW)
	GPIO.output(Motor4E,GPIO.LOW)
	return True
def SetAngle(angle):
	duty = angle/18+2
	GPIO.output(servo,True)
	pwm.ChangeDutyCycle(duty)
	time.sleep(1)
	GPIO.output(servo,False)
	pwm.ChangeDutyCycle(0)

def turn_left():
        angle = angle+45
        if(angle<=180):
                SetAngle(angle)

def right_left():
	angle = angle-45
	if(angle>=0):
                SetAngle(angle)

com1 = "dummy"
while(True):
	print("in")
	page = requests.get('https://shruthims.pythonanywhere.com/livestream/')
	tree = html.fromstring(page.content)
	command = tree.xpath('//div[@title="scraptitle"]/text()')
	print("commands: ", command)
	com = command[0][2:-1]
	if(com == "turnright") and (com1!=com):
		print(com)
		angle = angle+45
		if(angle<=270):
			SetAngle(angle)
		
		com1=com
	elif(com == "turnleft") and (com1!=com):
		print(com)
		angle = angle-45
		if(angle>=0):
                	SetAngle(angle)
		#turn_right()
		com1=com
	elif(com == "forward") and (com1!=com):
		print(com)
		forward()
		com1=com
	elif(com == "reverse") and (com1!=com):
		print(com)
		reverse()
		com1=com
	elif(com == "left") and (com1!=com):
		print(com)
		left_side()
		com1=com
	elif(com == "right") and (com1!=com):
		print(com)
		right_side()
		com1=com
	elif(com == "forward1") and (com1!=com):
		print(com)
		forward_1()
		com1=com
	elif(com == "reverse1") and (com1!=com):
		print(com)
		reverse_1()
		com1=com
	elif(com == "left1") and (com1!=com):
		print(com)
		left_side_1()
		com1=com
	elif(com == "right1") and (com1!=com):
		print(com)
		right_side_1()
		com1=com
	elif(com == "stop") and (com1!=com):
		print(com)
		stop()
		com1=com