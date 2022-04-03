import RPi.GPIO as GPIO

buttonPin = 12# pin for input signal from button switch 
ledPin = 11 # pin for output signal to LED


def setup():
    GPIO.setmode(GPIO.BOARD) # mode for physical GPIO numbering
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) #set buttonPin for input mode
    GPIO.setup(ledPin, GPIO.OUT) # set ledPin for output mode

    
def loop():
    while True:
        if GPIO.input(buttonPin)==GPIO.LOW: # ie. if button is pressed down to switch on
            GPIO.output(ledPin, GPIO.HIGH) # output signal to LED
            print('LED signal is turned on >>>')
        else:
            GPIO.output(ledPin, GPIO.LOW) # No output signal
            print('LED turned off >>>')
        
        
def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    print('Start Program')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()