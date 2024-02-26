num1 = float(input("Digite um número: >>> "))
num2 = float(input("Certo. Agora digite outro número: >>> "))
operador = input("Escolha um operador: +, -, *, / ")

if operador == "+":
    res = num1 + num2
    print(f"{num1} + {num2} = {res}")
elif operador == "-":
    res = num1 - num2
    print(f"{num1} - {num2} = {res}")
elif operador == "*":
    res = num1 * num2
    print(f"{num1} x {num2} = {res}")
elif operador == "/":
    res = num1 / num2
    print(f"{num1} / {num2} = {res}")
else:
    print("Invalido, encerrando programa...")