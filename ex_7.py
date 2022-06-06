"""
Crie um programa que solicite ao usuário a
operação desejada e implemente as quatro
operações matemáticas (soma, subtração,
multiplicação e divisão)

"""
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print("Escolha a opção da operação desejada:")

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

option= int (input("> Opção: "))

if option == 1:
  result = n1 + n2
  print(f"{n1} + {n2} = {result}")
elif option == 2:
  result = n1 - n2
  print(f"{n1} - {n2} = {result}")
elif option == 3:
  result = n1 * n2
  print(f"{n1} * {n2} = {result}")
elif option == 4:
  result = n1 / n2
  print(f"{n1} / {n2} = {result}")
else:
  print("Opção inválida")
