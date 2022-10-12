from bonequinhos import stages
from palavras import palavras
import os
import random

def jogarDnv():
    while True:
        print("\n\nVai querer jogar de novo meu amigo?")
        resp = input("Digite \"s\" para continuar ou \"n\" para sair:").lower()
        if resp == "s":

            break
        elif resp == "n":
            exit()
        else:
            os.system("cls")
            print("Desculpe, não entendi.")
    global a
    a = 1

while True:
    os.system("cls")
    print("Bem vindo ao jogo da Forca mais dificil do mundo.\nApenas escolha uma letra e eu te digo se acertou ou não.")
    i = m = a = 0
    t = 6
    tentativas = []
    palavMent = []
    palavraCerta = random.choice(palavras)
    palavC = list(palavraCerta)
    
    while m < len(palavraCerta):
        palavMent.insert(m,"_")
        m+=1


    while t > 0:
        print("Voce tem",t,"tentativas agora... cuidado.")
        print(stages[t])
        print(' '.join(palavMent))
        sera = letra = input("\nFaça sua escolha:").lower()
        os.system("cls")

        if letra == "sair":
            exit()
        if letra in tentativas:
            print("\nChutando a mesma letra? aaa para ne.\n")
        elif letra not in palavC:
            t-=1
            if t == 0:
                print(stages[0],"\nVixe amigo, perdeu ein.\nTudo bem, voce pode tentar de novo na próxima.\nPor via das dúvidas a palavra era",palavraCerta,end = ".")
                jogarDnv()
            else:
                print("\nHmm... sei não ein, acho que essa letra ai não tem.\n")  
        elif letra in palavC:
            while i < len(palavraCerta):

                if letra in palavC[i]:
                    palavMent[i]=letra
                i+=1
            print("\nIMPOSSIVEL, COMO VOCE SABE?\n")
            i=0
        if "_" not in palavMent or sera == palavraCerta:
            t = 0
            print(stages[6],"\nOQUE? COMO?\nCOMO VOCE GANHOU?\nOk, só conseguiu ganhar pq tava fácil.")
            jogarDnv()
        if a == 1:
            break
        tentativas.append(letra)