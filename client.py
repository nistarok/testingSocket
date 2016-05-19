import socket
import time

ip = raw_input('Manda o ip do servidor pa nois: ')
port = 7000
addr = ((ip,port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destination_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

destination_connected = False
try:
    dest_addr = ((ip,7002))
    destination_socket.connect(dest_addr)
    destination_connected = True
except:
    print "Ei amiguinho! Nao esquece de executar o destino pra descriptografar"


if destination_connected:
    count_try_connection = 0
    connected = False
    print 'Tentando conectar no servidor de criptografia'
    while (count_try_connection < 5 and connected is not True ):
        try:
            print 'Tentativa '+str(count_try_connection+1)+' no servidor 1'
            client_socket.connect(addr)
            connected = True
        except:
            time.sleep(5)
            count_try_connection +=1

    if not connected:
        count_try_connection = 0
        port = 7001
        addr = ((ip,port))
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while (count_try_connection < 5 and connected is not True ):
            try:
                print 'Tentativa '+str(count_try_connection+1)+' no servidor 2'
                client_socket.connect(addr)
                connected = True
            except:
                time.sleep(5)
                count_try_connection +=1

    if connected:
        msg = ""
        while not msg:
            msg = raw_input('Manda a mensagem pa nois: ')
            if not msg:
                print 'Escreve uma mensagem pa nois tio'
        client_socket.send(msg)
        data = client_socket.recv(1024)
        client_socket.close()

        print "Recebi a mensagem criptografada, mandando pro destino descriptografar"
        destination_socket.send(data)

        final_msg = destination_socket.recv(1024)
        destination_socket.close()
        print "Recebi a mensagem descriptografada"
        print "Mensagem descriptografada: "+final_msg
    else:
        print 'Nem consegui conectar no servidor :( '
