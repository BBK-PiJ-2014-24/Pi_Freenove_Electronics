# A SCRIPT THAT USES AN EVENT LISTENER FOR BUTTON ACTIVATION
# ----------------------------------------------------------

import RPi.GPIO as GPIO


buttonPin = 12# pin for input signal from button switch 
ledPin = 11 # pin for output signal to LED
ledState = False # flag for LED state


def setup():
    GPIO.setmode(GPIO.BOARD) # mode for physical GPIO numbering
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) #set buttonPin for input mode
    GPIO.setup(ledPin, GPIO.OUT) # set ledPin for output mode

# BUTTON EVENT LISTENER CALLBACK FN
def buttonEvent(channel):
    global ledState # use the global keyword if you want to change a global variable inside a function.
    print('buttonEvent GPIO-{}'.format(channel))
    ledState = not ledState
    if ledState:
        print('LED turned on >>>')
    else:
        print('LED turned off >>>')
    GPIO.output(ledPin, ledState) # Instead of using GPIO.HIGH or LOW just use boolean
    
def loop():
    # set up event listener first add_event_detect(listen for pin #, type pin action, bouncetime )
    GPIO.add_event_detect(buttonPin, GPIO.FALLING, callback = buttonEvent, bouncetime=300) # bouncetime is a delay for fat finger
    # set up infinite loop to keep event listener running indefinitely
    while True:
       pass # loop cannot be left empty just pass
        
def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    print('Start Program')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()