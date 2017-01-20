########################## blink.py ###########################################
# Author: Santiago Smith Silva
# Description:  This is a sample code to make a led blink
#               using the GPIO 14 declared as "led_pin"
###############################################################################
import RPi.GPIO as GPIO
import time

led_pin = 14
delay =1
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

try:
    while 1:
        print("LED is ON")
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(delay)
        print("LED is OFF")
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(delay)
except KeyboardInterrupt:
    GPIO.output(led_pin, GPIO.LOW);
    GPIO.cleanup()
    print("Lights OFF\n Bye!\n")

print("Done")
