from numero import numeros1_100
import os
import random
os.system("cls")
print("Neste programa você irá poder rolar vários tipos de dados.\nApenas escolha qual dos tipos de dados abaixo você deseja rolar.\n\nD3, D4, D6, D8, D12, D20, D100.")

while True:
    dado = input("Caso deseje sair digite 0.\n\nCaso contrário digite o número do dado que deseja e o resto é comigo:")
    os.system("cls")

    if dado in ["3","4","6","8","12","20","100"]:
        print("O resultado de sua rolada deu {}.\n".format(random.choice(numeros1_100[0:int(dado)])))
    elif dado == "0":
        break
    else:
        print("Não temos esse dado. :(\n")
    print("Quer rolar mais algum dado?")