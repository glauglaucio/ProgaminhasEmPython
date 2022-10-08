from bonequinhos import stages
from palavras import palavras
import os
os.system("cls")
import random
i = m = 0
t = 6
tentativas = []
palavMent = []
palavraCerta = random.choice(palavras)
palavC = list(palavraCerta)
print("Bem vindo ao jogo da Forca mais dificil do mundo\nApenas escolha uma letra e eu te digo se acertou ou não.")

while m < len(palavraCerta):
    palavMent.insert(m,"_")
    m+=1

while t > 0:
    print("Voce tem",t,"tentativas agora... cuidado.")
    print(stages[t])
    print(' '.join(palavMent))
    letra = input("\nFaça sua escolha:")
    os.system("cls")
    if letra in tentativas:
        print("\nchutando a mesma letra? aaa para ne\n")
    elif letra not in palavraCerta:
        t-=1
        if t == 0:
            print(stages[0],"\nVixe amigo, perdeu ein.\nTudo bem, voce pode tentar de novo na próxima.\nPor via das dúvidas a palavra era",palavraCerta,end = ".")
            break
        print("\nHmm... sei não ein, acho que essa letra ai não tem.\n")  
    elif letra in palavC:
        print("\nIMPOSSIVEL, COMO VOCE SABE?\n") 
        while i < len(palavraCerta):
            if letra in palavC[i]:
                palavMent[i]=letra
                if "_" not in palavMent:
                    t = 0
                    print(stages[6],"\nVOCE GANHOU, mas... como?")
                i+=1
            else:
                i+=1
        i=0  
    tentativas.append(letra)