#coding:utf-8
#@author Italo Modesto

import socket

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
door = 4444
server_address = (host, door)

tcp.bind(server_address)

tcp.listen(1)
print ("Servidor tcp iniciado no ip", host, "porta", door)

 
conn, client = tcp.accept()
print ("Conectado com: ", client)
	
while True:
	msg = conn.recv(1024)
	print("mensagem do cliente:", msg.decode(), "\n")
	
	if(msg.decode() == "close"):
		client.close()
		break
			
	response = input("Digite sua resposta: ")
	conn.send(str(response).encode())



