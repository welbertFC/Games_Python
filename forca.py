import  random
def jogo_forca():

    print("***********************************")
    print("Bem vindo ao jogo de forca")
    print("***********************************")


    arquivo = open("palavra.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip().upper()
        palavras.append(linha)


    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_" for letra in palavra_secreta]

 
    enforcou = False
    acertou = False
    erros = 0


    print(letras_acertadas)


    while(not enforcou and not  acertou):

        chute = input("Qual a letra  ?")
        chute = chute.strip().upper()


        if (chute in palavra_secreta):

            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
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