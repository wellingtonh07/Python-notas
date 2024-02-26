palavra_secreta = "Corinthians"
palpite = ""
contagem_palpites = 0
limite_palpites = 3
sem_palpites = False

#Vai executar o código até o palpite ser igual a palavra secreta
#E não estão sem palpites
while palpite != palavra_secreta and not(sem_palpites):
    #Verifica se ainda não usaram todos os palpites
    if contagem_palpites < limite_palpites:
        palpite = input("Digite uma palavra: >>> ")
        contagem_palpites += 1
        #Pra contar os palpites
    else:
        sem_palpites = True

#Caso erre os 3 palpites
if sem_palpites:
    print("Você perdeu")
else:
    print("Você conseguiu")