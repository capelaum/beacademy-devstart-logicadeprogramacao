"""
Crie um programa que receba do usuário um
número e apresente a Tabuada deste.
"""

number = int(input("Digite um número inteiro: "))

for i in range(1,11):
  print(f"{number} x {i} = {number*i}")
