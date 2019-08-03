import random

def jogo_adivinhacao():
    print("***********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("***********************************")

    numero_secreto = round(random.randrange(1,101))
    total_tentativas = 0
    pontos = 1000

    print("Qual nivel de dificuldade ?")
    print("Nivel 1: facil Nivel 2 medio Nivel 3 dificil")

    nivel = int(input("Defina um nivel: "))

    if (nivel ==1):
        total_tentativas = 20
    elif(nivel ==2):
        total_tentativas = 10
    else:
        total_tentativas = 5




    for rodada in range(1,total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute_str = input("Digite o seu numero: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100 ):
            print("Você deve digitar um numero entre 1 e 100")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou !!!!!", "Você fez {} pontos" .format(pontos))
            break
        else:
            if (maior):
                print("O seu chute foi maior que o numero secreto")
            elif (menor):
                print("O seu chute foi menor que o numero secreto")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos

    print("Fim de jogo")

if(__name__ == "__main__"):
    jogo_adivinhacao()
