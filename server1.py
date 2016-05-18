import socket
from simplecrypt import encrypt, decrypt

host = ''
port = 7000
recebe = "" #var. que recebe a mensagem
addr = (host, port)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.bind(addr)
serv_socket.listen(10) #limite de conexoes
print('Aguardando conexao...')
con, cliente = serv_socket.accept()
print('Conectado no servidor 1')
print('Aguardando uma mensagem do cliente')

# while not recebe:
recebe = con.recv(1024)
if recebe:
    ciphertext = encrypt('password', recebe)
    con.send(ciphertext)
serv_socket.close()
