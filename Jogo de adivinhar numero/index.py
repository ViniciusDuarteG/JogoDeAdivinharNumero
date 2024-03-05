import random

resposta = str

while resposta != "NÃO":
    
    resposta = str(input("Deseja jogar?\n")).upper().strip()
    
    if resposta == "NÃO" or resposta == "N" or resposta =="NO":
        break
    
    numero_maquina = random.randint(0,9)

    numero_jogador = int(input("Insira um número de 0 a 9:\n"))

    if numero_maquina != numero_jogador:
        print("A maquina jogou {0}, você jogou {1}".format(numero_maquina,numero_jogador))
        print("Você errou!")
        
    else:
        print("A maquina jogou {0}, você jogou {1}".format(numero_maquina,numero_jogador))
        print("Você acertou!")
    
    
    
print("Fim de jogo")