"""
Uma matriz quadrada é uma matriz que tem a mesma quantidade de linhas e colunas.

A diagonal principal é obtida pelos índices iguais de linhas e colunas.

A diagonal secundária pela seguinte regra:
A soma dos índices da linha e coluna é igual ao tamanho da matriz
menos um, ou seja, em uma Matriz de dimensão(tamanho)
3, sempre que a soma de seus índice forem 2, estamos na
diagonal secundária.

Dada esta explicação crie um programa que permita o
cadastro de uma Matriz e exiba a soma da diagonal
principal e secundária.
"""

matrix_size = int(input("Digite o tamanho da matriz: "))

if matrix_size < 2:
  print("O tamanho da matriz deve ser maior que 1")
  exit()

matrix = []
for i in range(matrix_size):
  my_list = []

  for j in range(matrix_size):
    my_list.append(int(input(f"Digite o valor da posição {i}, {j}: ")))

  matrix.append(my_list)

print(f"Matriz: {matrix}")

main_diagonal_sum = sum(matrix[i][i] for i in range(matrix_size))
secondary_diagonal_sum = sum(matrix[i][matrix_size - i - 1] for i in range(matrix_size))

print(f"Soma da diagonal principal: {main_diagonal_sum}")
print(f"Soma da diagonal secundária: {secondary_diagonal_sum}")
