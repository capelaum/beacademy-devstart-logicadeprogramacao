"""
Considere uma planilha de 5 linhas por 4
colunas, a qual será representada por uma matriz
bidimensional.

Desenvolva um programa que faça a leitura, a
partir do teclado, dos valores numéricos das
primeiras 4 linhas e 3 colunas da planilha.

Realizada a leitura, armazenar a soma dos
valores de cada linha na linha correspondente da
última coluna.

Finalmente, armazenar a soma dos valores de cada coluna
na coluna correspondente da última linha da planilha.

Imprima a planilha ao final.
"""

matrix = []

for i in range(4):
  my_list = []

  for j in range(3):
    my_list.append(int(input(f"Digite o valor da posição {i}, {j}: ")))

  matrix.append(my_list)

print(f"Matriz: {matrix}")

for i in range(4):
  row_sum = sum(matrix[i][j] for j in range(3))
  matrix[i].append(row_sum)

print(f"Matriz: {matrix}")

last_row = []
for i in range(4):
  col_sum = sum(matrix[j][i] for j in range(4))
  last_row.append(col_sum)

matrix.append(last_row)
print(f"Matriz: {matrix}")

print("\nPlanilha final:")

for i in range(5):
  for j in range(4):
    print(f"{matrix[i][j]} ", end="\n" if j == 3 else "")
