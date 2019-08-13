import serial
import requests

url = 'http://shruthims.pythonanywhere.com/livestream/coordinates/'
ser = serial.Serial('/dev/ttyACM0',9600)
while True:
	value = ser.readline()
	x = value.split()
	lat = str(x[0])
	lon = str(x[1].strip('\n'))
	payload = {'data': lat + ' ' + lon}
	r = requests.post(url, payload)
	print(r, payload)