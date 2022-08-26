import serial
import time
import string
import paho.mqtt.publish as publish
# reading and writing data from and to arduino serially.
ser = serial.Serial("/dev/rfcomm0", 9600)
ser.write(str.encode('Start\r\n'))
while True:
	if ser.in_waiting > 0:
		rawserial = ser.readline()
		cookedserial = rawserial.decode('utf-8').strip('\r\n')
		print(cookedserial)

		publish.single("test", cookedserial, hostname="13.54.84.169") 

		print("Done")
