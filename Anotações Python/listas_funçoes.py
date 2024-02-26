numeros_da_sorte = [3, 2, 1, 5, 9]
times = ["Corinthians", "Flamengo", "São Paulo", "Palmeiras"]

times.extend(numeros_da_sorte)
#2 listas em uma só
print(times)

times.append("Vasco")
#Adiciona a lista
print(times)

times.remove("Palmeiras")
#Remove da lista
print(times)

times.pop()
#Elimina o ultimo elemento da lista
print(times)

numeros_da_sorte.sort()
#Coloca em ordem crescente
print(numeros_da_sorte)

numeros_da_sorte.reverse()
#Lista em ordem contraria
print(numeros_da_sorte)

#times.clear()