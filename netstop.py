import network
n=network.WLAN(network.STA_IF)
n.active(False)
n=network.WLAN(network.AP_IF)
n.active(False)
