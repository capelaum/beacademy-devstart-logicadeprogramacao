"""
Crie um programa que, utilizando a estrutura escolha
caso, permita ao usuário escolher a operação a
realizar (depósito ou saque ou transferência), caso a
operação seja de transferência solicite o nome do
banco, da agência e conta, receba as informações e,
em ao final exiba o valor inicial, a operação realizada
e o saldo atual, no caso de transferência exiba
também os dados do banco, agência e conta.
"""

print("Escolha a operação:")
print("1 - Depósito")
print("2 - Saque")
print("3 - Transferência")

option = int(input("> Opção: "))

balance = 1000

if option == 1:
  value = float(input("Valor do depósito: "))

  print("-----------------------------")
  print("Operação realizada: Depósito")

  print(f"Saldo inicial: {balance}")
  balance += value
  print(f"Saldo atual: {balance}")
elif option == 2:
  value = float(input("Valor do saque: "))

  print("-----------------------------")
  print("Operação realizada: Saque")

  print(f"Saldo inicial: {balance}")
  balance -= value
  print(f"Saldo atual: {balance}")
elif option == 3:
  value = float(input("Valor da transferência: "))

  bank = input("Nome do Banco: ")
  agency = input("Agência: ")
  account = input("Conta: ")

  print("-----------------------------")
  print("Operação realizada: Transferência")

  print(f"Saldo inicial: {balance}")
  balance -= value
  print(f"Saldo atual: {balance}")

  print("Dados da transferência:")
  print(f"Banco: {bank}")
  print(f"Agência: {agency}")
  print(f"Conta: {account}")
else:
  print("Opção inválida")
