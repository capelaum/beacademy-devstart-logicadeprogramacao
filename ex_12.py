"""
Crie um programa que imprima os múltiplos
de 3 entre dois números digitados pelo
usuário.
"""

n1 = int(input("Digite o primeiro número inteiro:"))
n2 = int(input("Digite o segundo número inteiro:"))

for i in range(n1, n2+1):
  if i % 3 == 0:
    print(i)
