import socket

IP = '127.0.0.1'
PUERTO = 8083

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    cliente.connect((IP, PUERTO))
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Bienvenido a caliente, caliente")

    c_abierta = True
    while c_abierta:

        intro = (input(":"))
        intro = str.encode(intro)
        cliente.send(intro)
        msg = (cliente.recv(1000).decode('utf-8'))

        if msg == "Felicidades! Ha acertado el número":
            print(msg)
            cliente.close()
        else:
            print("Vuelva a introducirlo")


except KeyboardInterrupt:
    cliente.close()
    print('Cerrando la calculadora...')
