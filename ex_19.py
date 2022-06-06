"""
Crie um programa que permita cadastrar os seguintes dados de um Aluno:

Nome, nota1 e nota2.

Receba estes valores em vetores e
calcule e exiba ao final todos os dados e a
informação se o aluno foi aprovado(media
maior ou igual a 6) ou reprovado(media
inferior a 6).
"""

student = []
scores = []

for i in range(1, 4):
  student.append(input(f"\nInforme o nome do aluno {i}: "))
  scores.append(input(f"Informe a nota 1 do aluno {i}: "))
  scores.append(input(f"Informe a nota 2 do aluno {i}: "))

scoreCount = 0
for i in range(0, 3):
  print(f"\nNome: {student[i]}")

  print(f"Nota 1: {scores[scoreCount]}")
  print(f"Nota 2: {scores[scoreCount + 1]}")
  print(f"Média: {(float(scores[scoreCount]) + float(scores[scoreCount + 1]))/2}")
  scoreCount += 2
