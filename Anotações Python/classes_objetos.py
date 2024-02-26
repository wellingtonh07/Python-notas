#Importando a classe estudante feita em outro arquivo python
from estudante_classe import estudante

#Objeto que foi criado a partir da classe estudante, que está no arquivo estudante_classe.py
#Pode-se criar quantos objetos quiser
estudante_1 = estudante("Jim", "Negócios", 3.1, False)

print(estudante_1.nome)