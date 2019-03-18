import socket
import random
IP = '127.0.0.1'
PUERTO = 8083
num_respuestas = 99

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    servidor.bind((IP, PUERTO))
    servidor.listen(num_respuestas)
    print('Esperando conexion en {ip},{puerto}'.format(ip = IP, puerto = PUERTO))
    (cliente, direccion) = servidor.accept()
    print('Se ha conectado alguien')
    print("Escriba un número del 1 al 99")
    c_abierta = True
    while c_abierta:
        random = random.randint(0,99)
        intro = int(cliente.recv(1000).decode('utf-8'))

        if int(intro) == random:
            msg = "Felicidades! Ha acertado el número"
            msg = str.encode(msg)
            cliente.send(msg)

        elif (random-3 < int(intro) < random + 3):
            msg = "Caliente, caliente..."
            msg = str.encode(msg)

            cliente.send(msg)
        elif (random - 6 < int(intro)):
            msg = "Frio por abajo"
            msg = str.encode(msg)
            cliente.send(msg)
        elif (int(intro) < random + 6):
            msg = "Frío por arriba"
            msg = str.encode(msg)

            cliente.send(msg)

        c_abierta = False

except KeyboardInterrupt:
    cliente.close()
    print("Cerrando programa")
