import random

print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = random.randrange (1 , 101)
total_de_Tentativas = 20
rodada = 1

for rodada in range(1, total_de_Tentativas + 1):
    print("Tentativa: {} de {}".format(rodada, total_de_Tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)
    if(chute < 1 or chute > 100 ):
        print("Você deve digitar um número entre 1 e 100!")


    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou, Parabéns!")
        break
    else:
        if(maior):
            print("Você errou! o seu chute foi maior que o número secreto")
        elif(menor):
            print("Você errou! o seu chute foi menor que o número secreto")



print("Fim de Jogo")