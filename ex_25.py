"""
Faça um programa receba o salário do funcionário e
calcule o IRPF a ser pago conforme tabela abaixo.

- Até 1903,98            - Alíquota: Isento - Dedução: 0,00
- De 1903,99 até 2826,65 - Alíquota: 7.5%   - Dedução: 142,80
- De 2826,66 até 3751,05 - Alíquota: 15%    - Dedução: 354,80
- De 3751,06 até 4664,68 - Alíquota: 22,5%  - Dedução: 636,13
- Acima de 4664,68       - Alíquota: 27,5%  - Dedução: 869,36

Ao final imprima o valor do salário bruto o valor do
Imposto de Renda(IRPF) e o salário líquido.
"""

wage = float(input("Informe o salário mensal bruto: "))

if wage <= 1903.98:
  tax = 0
  tax_percent = 0
  deduction = 0
elif wage >= 1903.99 and wage <= 2826.65:
  tax = 0.075
  tax_percent = 7.5
  deduction = 142.80
elif wage >= 2826.66 and wage <= 3751.05:
  tax = 0.15
  tax_percent = 15
  deduction = 354.80
elif wage >= 3751.06 and wage <= 4664.68:
  tax = 0.225
  tax_percent = 22.5
  deduction = 636.13
elif wage > 4664.68:
  tax = 0.275
  tax_percent = 27.5
  deduction = 869.36

irpf = wage * tax

print("Salário bruto: R$ {:.2f}".format(wage))
print("Imposto de Renda: ({:.2f}%) R$ {:.2f}".format(tax_percent, irpf))
print("Dedução: R$ {:.2f}".format(deduction))
print("Salário líquido: R$ {:.2f}".format(wage - irpf))
