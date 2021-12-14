import network
import json
import time
from machine import Pin
import aabiot.LED
import Device
import aabiot

if aabiot.DoubleReset():
    print("Double Reset - Starting AP")
    AP()

#import settings
settings=json.loads(''.join(open('settings.json').readlines()))
LED=aabiot.LED.LED()

def netstop():
    n=network.WLAN(network.STA_IF)
    n.active(False)
    n=network.WLAN(network.AP_IF)
    n.active(False)

def STA():
    """Connects Board as Client to WiFi-Network. LED.Blinks 5 times short if successful and then displays the IP address in morse code"""
    sta=network.WLAN(network.STA_IF)
    if sta.isconnected():
        LED.Blink(5)
        return True
    sta.active(True)
    if ('NetMask') in settings and 'DNS' in settings and 'Gateway' in settings and 'IP' in settings:
        print("Static configuration active")
        sta.ifconfig((settings["IP"],settings["NetMask"],settings["Gateway"],settings["DNS"]))
    else:
        print("DHCP active")
    sta.connect(settings['ssid'],settings['password'])
    timeout=0
    while timeout < 30:
        if sta.isconnected():
            LED.Morse('ip %s'%sta.ifconfig()[0],1)
            return True
        else:
            LED.Blink(1,.05,.95)
            timeout += 1
            print("Time waiting: %s sec"%timeout)
    sta.active(False)
    return False

def AP():
    """Provides Access point with settings in settings.json. LED blinks 'AP' in morse code on success"""
    ap=network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=settings['AP-ssid'],password=settings['AP-password'])
    print("AP configured")
    LED.Morse ('AP')

netstop()
if STA() != True:
    AP()
Device.run()
