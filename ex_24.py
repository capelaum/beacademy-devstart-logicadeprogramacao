"""
Faça um programa para calcular a área e o perímetro
de um círculo. O usuário deve informar o valor do
raio do círculo.

Caso o raio seja um valor negativo,
deve-se informar uma mensagem de erro e solicitar
ao usuário que informe um novo valor. Utilize o valor
de 3,1416 para o pi.

Área = PI*Raio*Raio
Perímetro = 2*PI*Raio

Exiba ao final o valor do raio e o perímetro e a área.

"""

repeat = True

while repeat:
  radius = float(input("Informe o valor do raio: "))

  if radius < 0:
    print("O valor informado é inválido. Informe um valor positivo.")
    break

  pi = 3.1416
  area = pi * radius * radius
  perimeter = 2 * pi * radius

  print(f"Área: {area}")
  print(f"Perímetro: {perimeter}")

  repeat = False
