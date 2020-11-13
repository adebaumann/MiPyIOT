from machine import Pin
from time import sleep

class LED:
    """Define a LED on a defined pin"""
    def __init__(self,LEDPin=2):
        self.LEDPin=Pin(2,Pin.OUT)
        print ("New LED defined on Pin %s"%LEDPin)
    def Blink(self,number,timeon=0.2,timeoff=0.2):
        """Blinks the LED (number) times, (timeon) and (timeoff) are self explanatory"""
        for x in range (number):
            self.LEDPin.off()
            sleep(timeon)
            self.LEDPin.on()
            sleep(timeoff)

    def Pulse(self,seconds,Speed=1):
        """Helper function for Morse Code"""
        self.LEDPin.off()
        sleep(seconds)
        self.LEDPin.on()
        sleep (0.1*Speed)

    def Morse(self,text,Speed=1):
        """Blinks (text) in morse code. Speed is around 60 cpm at 1 and proportional"""
        Speed=1/Speed
        Dot=0.1*Speed
        Dash=0.3*Speed
        SpaceInLetter=0.1*Speed
        SpaceBetweenLetters=0.3*Speed
        Space=0.7*Speed
        alphabet={' ':' ','a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.',
                  'h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---',
                  'p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--',
                  'x':'-..-','y':'-.--','z':'--..','1':'.----','2':'..---','3':'...--','4':'....-',
                  '5':'.....','6':'-....','7':'--...','8':'---..','9':'----.','0':'-----',
                  '.':'.-.-.-',}

        print ("morsing %s"%text)
        for c in text:
            for m in alphabet[c.lower()]:
                if m == '.':
                    self.Pulse(Dot,Speed)
                if m == '-':
                    self.Pulse(Dash,Speed)
                if m == ' ':
                    sleep(Space)
            sleep(SpaceBetweenLetters)

