"""
Crie um programa que realize as 4 operações
matemática a partir de dois números que serão
digitados pelo usuário.

Após isto imprima os valores na tela e
em seguida pergunte se ele quer realizar novo cálculo,
repetido as operações enquanto o usuário desejar continuar.
"""

repeat = True

while repeat:
  n1 = float(input("Digite o primeiro número: "))
  n2 = float(input("Digite o segundo número: "))

  result = n1 + n2
  print(f"\nSOMA: {n1} + {n2} = {result}")

  result = n1 - n2
  print(f"SUBTRAÇÃO: {n1} - {n2} = {result}")

  result = n1 * n2
  print(f"MULTIPLICAÇÃO: {n1} * {n2} = {result}")

  result = n1 / n2
  print(f"DIVISÃO: {n1} / {n2} = {result}")

  repeat = input("\nDeseja realizar novo cálculo? (S/N) ").upper() == "S"
