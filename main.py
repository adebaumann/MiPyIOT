import network
import json
import time

settings=json.loads(''.join(open('settings.json').readlines()))

def netstop():
    n=network.WLAN(network.STA_IF)
    n.active(False)
    n=network.WLAN(network.AP_IF)
    n.active(False)
    
def STA():
    sta=network.WLAN(network.STA_IF)
    if sta.isconnected():
        return True
    sta.active(True)
    if ('NetMask') in settings and 'DNS' in settings and 'Gateway' in settings and 'IP' in settings:
        print("Static configuration active")
        sta.ifconfig((settings["IP"],settings["NetMask"],settings["Gateway"],settings["DNS"]))
    else:
        print("DHCP active")
    sta.connect(settings['ssid'],settings['password'])
    timeout=0
    while timeout < 60:
        if sta.isconnected():
            return True
        else:
            time.sleep(1)
            timeout += 1
            print("Time waiting: %s sec"%timeout)
    sta.active(False)
    return False

def AP():
    ap=network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=settings['AP-ssid'],password=settings['AP-password'])
    print("AP configured")

import garage
#garage.run()
