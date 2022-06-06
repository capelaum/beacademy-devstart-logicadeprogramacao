"""
Crie um programa que receba a altura e o peso
da pessoa e a classifique de acordo:

IMC < 19: Abaixo do Peso
19 <= IMC < 25: Peso Normal
25 <= IMC < 30: Sobrepeso
30 <= IMC < 40: Obesidade Tipo 1
40 <= IMC: Obesidade Mórbida

"""
weight = input("Digite seu peso (kg): ")
height = input("Digite sua altura (cm): ")

imc = float(weight) / (float(height) / 100) ** 2

print(f"IMC: {imc}")

if imc < 19:
  print("Abaixo do Peso")
elif imc >= 19 and imc < 25:
  print("Peso Normal")
elif imc >= 25 and imc < 30:
  print("Sobrepeso")
elif imc >= 30 and imc < 40:
  print("Obesidade Tipo 1")
else:
  print("Obesidade Mórbida")
