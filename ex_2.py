"""
Crie um programa que receba o nome e a idade de uma pessoa e exiba:

1. O nome e a idade informada;
2. Verdadeiro Se a idade é maior que 18;
3. Falso se a idade é diferente que 25;
4. Falso se a idade é diferente que 25 E o nome é igual a Marcos;
5. Verdadeiro se a idade é diferente que 25 OU o nome é igual a Marcos;
6. Verdadeiro se a idade dividida por 2 é igual a ZERO;

"""

name = input("Digite seu nome: ")
age = int(input("Digite sua idade: "))

if age > 18:
  print("Idade é maior que 18: Verdadeiro")

if age != 25:
  print("Idade é diferente de 25: Falso")

if age != 25 and name == "Marcos":
  print("Idade é diferente de 25 E o nome é igual a Marcos: Falso")

if age != 25 or name == "Marcos":
  print("Idade é diferente de 25 OU o nome é igual a Marcos: Verdadeiro")

if age % 2 == 0:
  print("Idade é divisível por 2: Verdadeiro")
