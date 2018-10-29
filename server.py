#coding:utf-8
#@author Italo Modesto
#https://wiki.python.org.br/SocketBasico

from __future__ import unicode_literals
import socket

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
door = 4444
server_address = (host, door)

tcp.bind(server_address)

tcp.listen(10)
print ("Servidor tcp iniciado no ip", host, "porta", door)

while True:
	conn, client = tcp.accept()
	print ("Conectado com: ", client)
	
	while True:
		msg = conn.recv(1024)
		print("mensagem do cliente: ")
		print(msg.decode())
	
		if(msg.decode() == "bye"):
			client.close()
			break
			
		response = raw_input("Digite sua resposta: ")
		conn.send(str(response).encode())



