import os
os.system("cls")
import random
print("SEJA BEM VINDO AO MAIOR CAMPEONATO DO MUNDO DE...")
print("\nPEDRA")
print("PAPEL")
print("OU TESOURAAAAAAAAAA")
print("\nQUAL VOCE VAI QUERER EIN MEU AMIGO? \nEU CONTRA VOCE NO MANO A MANO\nAQUI E AGORA")
doido = int(input("\nESCOLHA SABIAMENTE\nPARA PEDRA:1\nPARA PAPEL:2\nPARA TESOURA:3\n->"))
def pedra():
    print("\nVOCE ESCOLHEU PEDRA EIN?")
def papel():
    print("\nVOCE ESCOLHEU PAPEL EIN?")
def tesoura():
    print("\nVOCE ESCOLHEU TESOURA EIN?")
opcoes = {1:pedra, 3:tesoura, 2:papel}
opcoes.get(doido)()
kong = ["PEDRA","PAPEL","TESOURA"]
esckong = random.choice(kong)
print("MAS PARA O SEU IMPECILIO EU ESCOLHI",esckong)
if doido == 1 and esckong == "PEDRA":
    print("QUE? EMPATAMOS?")
elif doido == 1 and esckong == "PAPEL":
    print("XIII, MAS QUE MIXURUCA EIN, PERDESTE BOY")
elif doido == 1 and esckong == "TESOURA":
    print("CALMA... VOCE GANHOU CARA, COMO?")
elif doido == 2 and esckong == "PEDRA":
    print("CALMA... VOCE GANHOU CARA, COMO?")
elif doido == 2 and esckong == "PAPEL":
    print("QUE? EMPATAMOS?")
elif doido == 2 and esckong == "TESOURA":
    print("XIII, MAS QUE MIXURUCA EIN, PERDESTE BOY")
elif doido == 3 and esckong == "PEDRA":
    print("XIII, MAS QUE MIXURUCA EIN, PERDESTE BOY")
elif doido == 3 and esckong == "PAPEL":
    print("CALMA... VOCE GANHOU CARA, COMO?")
elif doido == 3 and esckong == "TESOURA":
    print("QUE? EMPATAMOS?")