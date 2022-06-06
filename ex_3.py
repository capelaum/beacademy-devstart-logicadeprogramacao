"""
Crie um programa que receba um valor de depósito
do usuário e atualize o seu saldo. Ao final exiba o
valor inicial o depósito e o saldo atual.

"""
deposit = input("Digite o valor do depósito: ")

balance = 1000

print(f"Saldo inicial: {balance}")
balance += int(deposit)
print(f"Saldo atual: {balance}")
