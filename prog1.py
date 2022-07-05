
import numpy as np
import socket
import pickle as pc
import time

size = int(input('Digite o tamanho desejado da matriz quadrada:'))
quant = int(input('Digite a quantidade de matrizes:'))


for i in range(quant):

	matriz = np.random.randint(100, size=(size, size))
	print(matriz)
	sec = time.time()
	list = [sec, matriz]
	list = pc.dumps(list)

	HOST = '192.168.121.2'
	PORT = 5000

	udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	dest = (HOST, PORT)

	udp.sendto (list, dest)
	udp.close ()

	print ('Enviado')
	print (sec)
