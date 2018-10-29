# TCP_Server-Python-
Procedimeto:

	SERVIDOR: abre porta (com endereço ip e porta) 
	SERVIDOR: fica ouvindo requisições de conexão 
	CLIENTE: solicita conexao 
	SERVIDOR: aceita a conexao, criando um conn (obj p enviar e receber respostas) e adrr (endereço do outro socket) 
	CLIENTE: digita mensagem, converte pra string, codifica e envia 
	SERVIDOR: recebe, decodifica e imprime 

	CLIENTE: fica guardando...
	SERVIDOR: digita msg, converte para string, codifica e envia.
	CLIENTE: recebe msg, imprime e reinicial o ciclo
