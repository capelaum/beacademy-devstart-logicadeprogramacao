"""
Crie um programa que receba do usuário a
figura geométrica que deseja calcular a área e
o perímetro (Q-Quadrado ou T-Triângulo) e
calcule e exiba a área e o perímetro da figura escolhida.
"""

import math

print("Escolha a figura geométrica:")
print("Q - Quadrado")
print("T - Triângulo")

option = input("> Opção: ")
side = float(input("Digite o tamanho dos lados: "))

if option == "Q":
  area = side * side
  perimeter = 4 * side
  print(f"A área do quadrado é {area} e o perímetro é {perimeter}")
elif option == "T":
  area = (side ** 2) * math.sqrt(3) / 4
  perimeter = 3 * side
  print(f"A área do triângulo é {area} e o perímetro é {perimeter}")
else:
  print("Opção inválida")
