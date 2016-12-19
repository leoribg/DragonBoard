import requests
import serial
from time import sleep

# Use as default
PORT = "/dev/ttyACM0"

def connectMote(port):
	try:
		ser = serial.Serial(port, 9600,timeout=0, parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
		print 'usb OK'
	except:
		print 'Error connecting to the USB device, aborting'
	return ser

def process_data(raw):
	# Search for start and end of frame and slice, discard incomplete
	if "\r\n" in raw:
		raw = raw.split("\r\n")
		print 'raw: '
		print raw[0]
		try:
			url = 'https://api.thingspeak.com/update?api_key=WGAESYN974EPF93V&field1=%s' % (raw[0])
    			r=requests.get(url)
			print 'sent to thingspeak'
		except:
			print 'problem in thingspeak'
			return

if __name__ == '__main__':

	s = connectMote(PORT)
	
	while True:
		queue = s.inWaiting()
		if queue > 0:
			data = s.read(1000)
			process_data(data)
		sleep(0.2)
