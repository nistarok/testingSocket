import socket
from simplecrypt import encrypt, decrypt

host = ''
port = 7002
recebe = "" #var. que recebe a mensagem
addr = (host, port)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.bind(addr)
serv_socket.listen(10) #limite de conexoes
print('Aguardando conexao...')
con, cliente = serv_socket.accept()
print('O destino ta ligado \n')
print('Aguardando uma mensagem para descriptografar')

# while not recebe:
recebe = con.recv(1024)
if recebe:
    deciphertext = decrypt('password', recebe)
    print " A mensagem eh : "+deciphertext
    con.send(deciphertext)

serv_socket.close()
