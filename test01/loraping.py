from network import LoRa
import socket
import time

#lora = LoRa(mode=LoRa.LORA, frequency=863000000)
lora = LoRa(mode=LoRa.LORA)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

def run():
    while True:
        s.send('Ping')
        buf = s.recv(64)
        if buf:
            print("recv=",buf)
        time.sleep(.5)
