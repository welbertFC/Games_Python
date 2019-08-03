import forca
import  adivinhacao
print("***********************************")
print("******Escolha o seu jogo***********")
print("***********************************")

print("jogos (1) Forca  (2) Adivinhação")

jogo = int(input("Qual jogo ?"))

if(jogo == 1):
    print("Jogo da forca")
    forca.jogo_forca()
elif(jogo ==2):
    print("jogo de adivinhação")
    adivinhacao.jogo_adivinhacao()


