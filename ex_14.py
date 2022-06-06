"""
Utilizando a estrutura de repetição while

Crie um programa que, imprima a tabuada de um
número digitado pelo usuário.
"""

number = int(input("Digite um número inteiro: "))

count = 1

while count < 11:
  print(f"{number} x {count} = {number*count}")
  count += 1
