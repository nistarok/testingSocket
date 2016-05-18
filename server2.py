import socket
from simplecrypt import encrypt, decrypt

host = ''
port = 7001
recebe = "" #var. que recebe a mensagem
addr = (host, port)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.bind(addr)
serv_socket.listen(10) #limite de conexoes
print('Aguardando conexao...')
con, cliente = serv_socket.accept()
print('Conectado no servidor 2')
print('Aguardando uma mensagem do cliente')

# while not recebe:
recebe = con.recv(1024)

ciphertext = encrypt('palavrapasse', recebe)
con.send(ciphertext)
print "Recebi criptografei e respondi. tchau"
serv_socket.close()
