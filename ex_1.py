"""
Crie um programa que declare 3 variáveis
para receber o Nome, o peso e a altura de uma pessoa.

Ao final imprima os dados na tela,
além de calcular e exibir também o Índice de Massa Corpórea(IMC) da pessoa.
"""


name = input("Digite seu nome: ")
weight = input("Digite seu peso (kg): ")
height = input("Digite sua altura (cm): ")

imc = float(weight) / (float(height) / 100) ** 2

print("----------------------------------")

print(f"Nome: {name}")
print(f"Peso: {weight}")
print(f"Altura: {height}")
print(f"IMC: {imc}")
