# Wifi Configuration
#
import machine
from network import WLAN
import time

_wlan = WLAN(mode=WLAN.STA)


# connect to wifi
def connect():
    global wifi_config,  _wlan

    nets = _wlan.scan()
    for net in nets:
        if net.ssid == wifi_config.name:
            print('Wifi: network %s found.' % net.ssid)
            _wlan.connect(net.ssid, auth=(net.sec, wifi_config.password), timeout=5000)
            tries=15
            for i in range(tries):
                print("%d/%d. Trying to connect." %(i+1, tries))
                machine.idle()
                time.sleep(1)
                if _wlan.isconnected(): break
            break

    if _wlan.isconnected():
        print('Wifi: connection succeeded!')
        print(_wlan.ifconfig())
    else:
        print('Wifi: connection failed!')
        accesspoint()

def accesspoint():
    global _wlan

    print('Wifi: activating accesspoint.')
    _wlan = WLAN(mode=WLAN.AP)

def connected():
    return _wlan.isconnected()
    
def config():
    return _wlan.ifconfig()
    
def delete():
    import os
    os.remove("wifi_config.py")
    # TODO: clear internal wifi assignment
    accesspoint()
    
def remove():
    delete()
    
def scan():
    nets = _wlan.scan()
    l=[]
    for n in nets:
        l.append( n.ssid )
    return l


# write config and connect
def setup( name,  password ):
    global wifi_config

    f=open("wifi_config.py", "w")
    f.write("name=\"%s\"\npassword=\"%s\"" % (name,password))
    f.close()
    wifi_config.name = name
    wifi_config.password = password
    connect()
    
# Try to find wifi_config
try:
    import wifi_config
    connect()
except ImportError:
    class wifi_config():
        pass
