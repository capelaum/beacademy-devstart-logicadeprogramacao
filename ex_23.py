"""
Faça um programa que receba o salário do funcionário e
aplique um desconto conforme os valores abaixo:

- até 1212,00: 7.5%
- de 1212,01 até 2427,35: 9%
- de 2427,36 até 3641,03: 12%
- de 3641,04 até 7087,22: 14%

Ao final imprima o valor do salário bruto o valor do
desconto e o salário líquido.

"""
wage = float(input("Informe o valor de seu salário: "))

if wage <= 1212:
  discount = wage * 0.075
  discount_percent = 7.5
elif wage <= 2427.35:
  discount = wage * 0.09
  discount_percent = 9
elif wage <= 3641.03:
  discount = wage * 0.12
  discount_percent = 12
elif wage <= 7087.22:
  discount = wage * 0.14
  discount_percent = 14
else:
  discount = wage * 0.15
  discount_percent = 15

wage_with_discount = wage - discount

print(f"Salário bruto: {'{0:,.2f}'.format(wage)}")
print(f"Desconto ({discount_percent}%): {'{0:,.2f}'.format(discount)}")
print(f"Salário líquido: {'{0:,.2f}'.format(wage_with_discount)}")
