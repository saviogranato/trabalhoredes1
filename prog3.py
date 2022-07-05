import socket
import numpy as np
import pickle as pc
import time

HOST1 = ''
PORT1 = 5000

udp1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST1, PORT1)
udp1.bind (orig)

while True:
    list, prog2 = udp1.recvfrom (1024)
    list = pc.loads(list)
    print ('Matriz Inversa:',list[0])
    print ('Determinante:',list[1])
    print ('Tempo total:',time.time()-list[2])

 
udp1.close ()
