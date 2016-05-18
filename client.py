import socket
from simplecrypt import encrypt, decrypt

ip = raw_input('Manda o ip do servidor pa nois: ')
port = 7000
addr = ((ip,port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

count_try_connection = 0
connected = False

while (count_try_connection and connected is not True ):
    try:
        client_socket.connect(addr)
        connected = True
    except:
        count_try_connection +=1

if connected:
    msg = raw_input('Manda a mensagem pa nois: ')

    ciphertext = encrypt('password', msg)
    deciphertext = decrypt('password', ciphertext)
    print deciphertext
else:
    print 'Nem consegui conectar no servidor :( '
