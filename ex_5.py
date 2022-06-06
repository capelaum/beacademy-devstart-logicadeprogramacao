"""
Crie um programa que receba a idade da
pessoa e a classifique de acordo:

- Menor que 18 anos: Menor de idade
- Entre 18 e 60 anos: Adulto
- Maior que 60 anos: Idoso

"""
age = int(input("Digite sua idade: "))

if age < 18:
  print("Menor de idade")
elif age >= 18 and age < 60:
  print("Adulto")
else:
  print("Idoso")
