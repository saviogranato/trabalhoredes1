import socket
import pickle as pc
import numpy as np


HOST = ''
PORT = 5000
HOST1 = '192.168.121.66'
PORT1 = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (HOST, PORT)



udp.bind (orig)
while True:
    list, prog1 = udp.recvfrom (1024)
    list = pc.loads(list)
    matriz = list [1]
    matriz_inv = np.linalg.inv(matriz)
    det = np.linalg.det(matriz_inv)
    print (det, prog1)
    list1 = pc.dumps([matriz_inv, det, list[0]])
    udp1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest = (HOST1, PORT1)
    udp1.sendto(list1, dest)
    udp1.close()
udp.close ()
