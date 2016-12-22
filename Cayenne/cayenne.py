import paho.mqtt.client as paho
from gpio_96boards import GPIO
import serial
from time import sleep

Username = 'USERNAME'
Password = 'PASSWORD'
clientID = 'CLIENT ID'

# Use as default
PORT = "/dev/ttyACM2"

def connectMote(port):
	try:
		ser = serial.Serial(port, 9600,timeout=0.3, parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
		print 'usb OK'
	except:
		print 'Error connecting to the USB device, aborting'
	return ser

GPIO_A = GPIO.gpio_id('GPIO_A')
pins = (
    (GPIO_A, 'out'),
)

payloadSensor = 'time,msec='

global laststatus
laststatus = 0

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))
 
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload)) 
	if(msg.topic == 'v1/' + Username + '/things/' + clientID + '/cmd/channel'):
        payload = str(msg.payload).split(",")
        client.publish('v1/'+ Username +'/things/' + clientID + '/data/channel', payload[1], qos=0)
		status = int(payload[1])
		with GPIO(pins) as gpio:
        		if(status):
					gpio.digital_write(GPIO_A, GPIO.HIGH)
					print 'turn ON'
					laststatus = payload 
				else:
					gpio.digital_write(GPIO_A, GPIO.LOW)
					print 'turn OFF'
					laststatus = payload

#Connect to Cayenne
client = paho.Client(client_id=clientID)
client.on_publish = on_publish
client.on_subscribe = on_subscribe
client.on_message = on_message
client.username_pw_set(Username, Password)
client.connect(host='mqtt.mydevices.com', port=1883, keepalive=60)
client.subscribe(('v1/' + Username + '/things/' + clientID + '/cmd/channel', 0))

client.loop_start()

if __name__ == '__main__':
	s = connectMote(PORT)
	while True:
		queue = s.inWaiting()
		if queue > 0:
			data = s.read(10)
			if "\r\n" in data:
				print data
				try:
					post  = payloadSensor + data
					client.publish('v1/' + Username + '/things/' + clientID + '/data/channel', post, qos=0)
					print 'sent to Cayenne'
				except:
					print 'problem in Cayenne'
