try:
    valor = 10/0
    #Nenhum número se divide por 0
    num = int(input("Digite um número: > "))
    print(num)
except ZeroDivisionError:
    print("Não divide por 0")
except ValueError:
    print("Entrada invalida")

#Tem o objetivo de contornar possiveis erros mostrados no console