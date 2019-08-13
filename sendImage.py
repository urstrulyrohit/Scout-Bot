import os
import base64
import time
import requests
import cv2.cv as cv
#url = 'http://127.0.0.1:8000/scoutbot/saveFrame'
url = 'http://shruthims.pythonanywhere.com/livestream/saveFrame/'

capture = cv.CaptureFromCAM(-1)

while True:
    img = cv.QueryFrame(capture)
    cv.SaveImage('ele.jpg', img) 
    filename = "ele.jpg"
    with open(filename,"rb") as image_file:
	encoded_string = str(base64.b64encode(image_file.read()))
	payload = {'data':encoded_string}
	r = requests.post(url, data = payload)
	print("posted")
	#print(encoded_string)