from operator import le
from bonequinhos import stages
from palavras import palavras
import os
import random
os.system("cls")
i = m = 0
t = 6
tentativas = []
palavMent = []
palavraCerta = random.choice(palavras)
palavC = list(palavraCerta)
print("Bem vindo ao jogo da Forca mais dificil do mundo.\nApenas escolha uma letra e eu te digo se acertou ou não.")

while m < len(palavraCerta):
    palavMent.insert(m,"_")
    m+=1

while t > 0:
    print("Voce tem",t,"tentativas agora... cuidado.")
    print(stages[t])
    print(' '.join(palavMent))
    letra = input("\nFaça sua escolha:").lower()
    os.system("cls")
    print(letra)
    print(tentativas)
    if letra in tentativas:
        print("\nChutando a mesma letra? aaa para ne.\n")
    elif letra not in palavC:
        t-=1
        if t == 0:
            print(stages[0],"\nVixe amigo, perdeu ein.\nTudo bem, voce pode tentar de novo na próxima.\nPor via das dúvidas a palavra era",palavraCerta,end = ".")
            exit()
        print("\nHmm... sei não ein, acho que essa letra ai não tem.\n")  
    elif letra in palavC:
        while i < len(palavraCerta):
            if letra in palavC[i]:
                palavMent[i]=letra
                if "_" not in palavMent:
                    t = 0
                    print(stages[6],"\nOQUE? COMO?\nCOMO VOCE GANHOU?\nOk, só conseguiu ganhar pq tava fácil.")
                i+=1
            else:
                i+=1
        if t != 0: print("\nIMPOSSIVEL, COMO VOCE SABE?\n")
        i=0  
    tentativas.extend(letra)