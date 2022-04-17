import RPi.GPIO as GPIO
import time

ledPins = [11, 12, 13, 15, 16, 18, 22, 3, 5, 24]

def setup():
    GPIO.setmode(GPIO.BOARD) # use Physical GPIO Numbering
    GPIO.setup(ledPins, GPIO.OUT) # set all ledPins to OUTPUT mode
    GPIO.output(ledPins, GPIO.HIGH) # All LEDs are initially start with lights on.

def loop():
    while True:
        for pin in ledPins:
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(pin, GPIO.HIGH)
        # [::-1] => an unspecified start and finish implies implies the whole list. And -1 means to count backwards.
        for pin in ledPins[::-1]: 
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.1)

def destroy():
    GPIO.cleanup()
    
if __name__ == '__main__':
    print('Program is starting....')
    setup()
    try:
        loop()
    except KeyboardInterrupt: 
        destroy()
