from network import LoRa
import socket
import time

lora = LoRa(mode=LoRa.LORA, frequency=863000000)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

def run():
    while True:
        if s.recv(64) == b'Ping':
            s.send('Pong2')
        time.sleep(5)
