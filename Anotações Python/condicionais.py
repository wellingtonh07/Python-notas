#Executa quando a função for verdadeira

sexo_masculino = True
alto = True

#Se ou uma ou outra for verdadeira, executa
if sexo_masculino or alto:
    print("Você é homem, ou alto ou ambos")
#Not - nega o que esteja dentro do parentese
elif sexo_masculino and not(alto):
    print("Você é um homem baixo")
elif not(sexo_masculino) and alto:
    print("Você não é homem mas é alto")
else:
    print("Você não é homem e nem alto")

#Executa apenas se as 2 forem verdadeiras
#if sexo_masculino and alto:
  #  print("Você é homem e alto")
#else:
 #   print("Você não é homem e nem alto")