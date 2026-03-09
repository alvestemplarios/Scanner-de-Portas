import socket

alvo = input("Digite o IP ou site para escanear: ")

print("Escaneando portas...")

for porta in range(1, 1025):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.5)

    resultado = cliente.connect_ex((alvo, porta))

    if resultado == 0:
        print("Porta aberta:", porta)

    cliente.close()

print("Escaneamento finalizado.")