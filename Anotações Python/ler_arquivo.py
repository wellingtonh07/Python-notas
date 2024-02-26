f = open("teste.txt", "r")
#open = abre o arquivo
#r = read = ler
print(f.read())
#mostra o arquivo aberto no console

print(f.readline())
#Lê a primeira linha, se quiser ler mais linhas, repita o código

f.close()
#Fecha o arquivo - boa pratica