from network import LoRa
import socket
import time
import pycom


lora = LoRa(mode=LoRa.LORA)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
pycom.heartbeat(False)
pycom.rgbled(0x5f5f5f) # signal ready in white

def run():
    c = True
    while True:
        r=s.recv(64)
        print("Received:", r)
        received = False
        if r == b'Ping':
            s.send('Pong2')
            pycom.rgbled(0x00005f) # signal reception in blue
            received = True
        if c:
            if received:
                pycom.rgbled(0x00005f)
            else:
                pycom.rgbled(0x5f0000)
            c = False
        else:
            if received:
                pycom.rgbled(0x005f00)
            else:
              pycom.rgbled(0x5f5f5f)
            c = True
            
        time.sleep(1)
