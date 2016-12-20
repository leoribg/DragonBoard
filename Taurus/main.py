#!/usr/bin/python
import time
import requests
import taurus

from gpio_96boards import GPIO

global laststatus
laststatus = 0

GPIO_A = GPIO.gpio_id('GPIO_A')
pins = (
    (GPIO_A, 'out'),
)

taurus.taurus('SERIAL')

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Blink LED on GPIO A (pin 23)')
    args = parser.parse_args()

    with GPIO(pins) as gpio:
	while True:
		status = taurus.read_dActuator('1001')# put your actuator ID
		if(status and laststatus == 0):
			gpio.digital_write(GPIO_A, GPIO.HIGH)
			print 'turn ON'
			laststatus = status
		elif(status == 0 and laststatus):
			gpio.digital_write(GPIO_A, GPIO.LOW)
			print 'turn OFF'
			laststatus = status

