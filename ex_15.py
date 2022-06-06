"""
Crie um programa que solicite ao usuário o seu
nome e senha do cartão e valide se a senha e
nome são corretos

(Nome: Marcos e senha: paylivre)

Em caso positivo, dê boas vindas ao usuário
Em caso negativo, solicite os dados novamente.

"""

login = False

while not login:
  name = input("Digite o nome: ")
  password = input("Digite a senha: ")

  if name == 'Marcos' and password == 'paylivre':
    login = True
    print("\nBem vindo(a)!\n")
  else:
    print("\nNome ou senha incorretos, por favor tente novamente.\n")
