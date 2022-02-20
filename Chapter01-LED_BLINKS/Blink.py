import RPi.GPIO as GPIO
import time

ledPin = 11 

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)
    print ('using pin%d' %ledPin)

def loop():
    GPIO.output(ledPin, GPIO.HIGH)
    print ('LED turned on >>>')
    time.sleep(1)
    GPIO.output(ledPin, GPIO.LOW)
    print('LED turned off >>>')
    time.sleep(1)

def destroy():
    GPIO.cleanup()
    
if __name__ == '__main__':  
    print('Program Starting...\n')  
    setup()
    try:
        loop()
    except KeyboardInterrupt: #press ctrl-C to break
        destroy()