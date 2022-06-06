"""
Crie um programa que permita ao usuário tentar logar
em seu Sistema informando seu nome e senha. Repita a
operação até que o nome e senha correspondam a um
valor armazenado (Marcos – 1234).

Caso o usuário digite -1 interrompa a repetição e informe que o
programa será finalizado por solicitação do usuário.

"""

repeat = True

while repeat:
  name = input("Digite o nome: ")

  if name == '-1':
    repeat = False
    print("\nPrograma finalizado por solicitação do usuário.\n")
    break

  password = input("Digite a senha: ")

  if password == '-1':
    repeat = False
    print("\nPrograma finalizado por solicitação do usuário.\n")
    break

  if name == 'Marcos' and password == 'paylivre':
    repeat = False
    print("\nBem vindo(a)!\n")
  else:
    print("\nNome ou senha incorretos, por favor tente novamente.\n")
