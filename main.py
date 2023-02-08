from People import Pessoas

print("*****Apenas maiores de 18 anos!*****")
nome = input("digite seu nome:")
idade = int(input("digite sua idade:"))

pessoa = Pessoas(nome, idade)

print(pessoa.nome, "nasceu em", pessoa.idade - 2023)

if (pessoa.idade >= 18):
  print("Você tem acesso a esta página.")
else:
  print("Você ainda não é maior de idade, por tanto, não tem, acesso a essa página.")
