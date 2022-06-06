"""
Crie um programa inicie o saldo do cliente com R$
1000,00 e que permita o saques consecutivos no valor
de R$ 150.00 até que seu saldo seja positivo.

Quando isto ocorrer interrompa a operação e informe
que o saque não pode ser efetuado em razão de que o
saldo era insuficiente para efetuar a operação
"""

balance = 1000
print("Saldo inicial: " + str(balance))

repeat = True

while repeat:
  withdraw = input("Deseja sacar R$150,00 (S/N)? ").upper() == "S"

  if withdraw:
    result = balance - 150

    if result < 0:
      repeat = False
      print("\nSaldo insuficiente para efetuar saque.\n")
      break

    balance = result
    print("Saldo atual: " + str(balance))
  else:
    repeat = False
    print("\nOperação cancelada pelo usuário.\n")
