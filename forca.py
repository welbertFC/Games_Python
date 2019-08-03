import  random

def jogo_forca():

    mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0


    while(not enforcou and not  acertou):

        chute = pede_chute(chute,letras_acertadas,palavra_secreta)


        if (chute in palavra_secreta):
            marca_chute_correto()


        else:
            print("ops você errou ainda falta {} tentativas".format(5-erros))
            erros += 1
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Parabens você ganhou")
    else:
        resposta = input("que pena você perdeu, quer tentar nocamente ? digite sim ou não")
        if(resposta == "sim"):
            jogo_forca()
        else:


            print("Fim de jogo")

if(__name__ == "__main__"):
    jogo_forca()


def mensagem_abertura():
    print("***********************************")
    print("Bem vindo ao jogo de forca")
    print("***********************************")

def carrega_palavra_secreta():
    arquivo = open("palavra.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip().upper()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def pede_chute():
    chute =input("Qual a letra  ?")
    chute = chute.strip().upper()

def marca_chute_correto(chute,letras_acertadas,palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1