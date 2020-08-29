from machine import Pin
from time import sleep

LEDPin=Pin(2,Pin.OUT)

def Blink(number,timeon=0.2,timeoff=0.2):
    n=0
    while n<number:
        LEDPin.off()
        sleep(timeon)
        LEDPin.on()
        sleep(timeoff)
        n +=1

def Pulse(seconds,Speed):
    LEDPin.off()
    sleep(seconds)
    LEDPin.on()
    sleep (0.1*Speed)

def Morse(text,Speed=1):
    Speed=1/Speed
    Dot=0.1*Speed
    Dash=0.3*Speed
    SpaceInLetter=0.1*Speed
    SpaceBetweenLetters=0.3*Speed
    Space=0.7*Speed
    alphabet={' ':' ',
              'a':'.-',
              'b':'-...',
              'c':'-.-.',
              'd':'-..',
              'e':'.',
              'f':'..-.',
              'g':'--.',
              'h':'....',
              'i':'..',
              'j':'.---',
              'k':'-.-',
              'l':'.-..',
              'm':'--',
              'n':'-.',
              'o':'---',
              'p':'.--.',
              'q':'--.-',
              'r':'.-.',
              's':'...',
              't':'-',
              'u':'..-',
              'v':'...-',
              'w':'.--',
              'x':'-..-',
              'y':'-.--',
              'z':'--..',
              '1':'.----',
              '2':'..---',
              '3':'...--',
              '4':'....-',
              '5':'.....',
              '6':'-....',
              '7':'--...',
              '8':'---..',
              '9':'----.',
              '0':'-----',
              '.':'.-.-.-',
              }
    print ("morsing %s"%text)
    for c in text:
        for m in alphabet[c.lower()]:
            if m == '.':
                Pulse(Dot,Speed)
            if m == '-':
                Pulse(Dash,Speed)
            if m == ' ':
                sleep(Space)
        sleep(SpaceBetweenLetters)
