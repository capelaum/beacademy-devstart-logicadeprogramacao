"""
Crie um programa que permita ao usuário escolher a
operação a realizar (depósito ou saque), receba a
informação da operação escolhida e o valor do
usuário e, em seguida, atualize o seu saldo.

Ao final exiba o valor inicial, a operação realizada e o saldo atual.
"""

print("Escolha a operação:")
print("1 - Depósito")
print("2 - Saque")

option = int(input("> Opção: "))

balance = 1000

if option == 1:
  value = float(input("Valor do depósito: "))
  print(f"Saldo inicial: {balance}")
  balance += value
  print(f"Saldo atual: {balance}")

if option == 2:
  value = float(input("Valor do saque: "))
  print(f"Saldo inicial: {balance}")
  balance -= value
  print(f"Saldo atual: {balance}")

if option != 1 and option != 2:
  print("Opção inválida")
