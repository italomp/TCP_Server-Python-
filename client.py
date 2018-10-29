#coding:utf-8
#@author Italo Modesto

from __future__ import unicode_literals
import socket

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
door = 4444
server_address = (host, door)

tcp.connect(server_address)

while True:
	msg = raw_input("Digite sua mensagem: ")
	tcp.send(str(msg).encode())

	response = tcp.recv(1024)

	if(response.decode == "bye"):
		tcp.colse()

	print("Resposta do servidor: ")
	print(response.decode())
