#PiLedTest.py - Exercise 2
print("PiLedTest.py is running on the Raspberry Pi")

import RPi.GPIO as GPIO
from time import sleep, time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(22,GPIO.IN)



while True:
    if GPIO.input(22) == 1:
        GPIO.output(24, GPIO.HIGH)
        sleep(0.1)

        GPIO.output(24, GPIO.LOW)
        sleep(0.1)

    else:
        end_time = time() + 5
        while time() < end_time:
            GPIO.output(24, GPIO.HIGH)
            sleep(0.05)

            GPIO.output(24,GPIO.LOW)
            sleep(0.05)
            
        GPIO.output(24, GPIO.LOW)

        while GPIO.input(22) == 0:
            sleep(0.1)

        