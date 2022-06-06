"""
Crie um programa que permita ao usuário
cadastrar 5 clientes com os seguintes dados:

- Nome;
- CPF;
- RG;
- Endereço; e
- Telefone.

Guarde os dados dos clientes em um vetor e ao final exiba-os.

"""

client = dict()
clients = list()

for i in range(1, 6):
  print(f"\nDados do Cliente {i}")

  client["name"] = input("Digite o Nome: ")
  client["cpf"] = input("Digite o CPF: ")
  client["rg"] = input("Digite o RG: ")
  client["address"] = input("Digite o Endereço: ")
  client["phone"] = input("Digite o Telefone: ")

  clients.append(client.copy())

for i, client in enumerate(clients):
  print(f"\nDados do Cliente {i + 1}")

  print(f"Nome: {client['name']}")
  print(f"CPF: {client['cpf']}")
  print(f"RG: {client['rg']}")
  print(f"Endereço: {client['address']}")
  print(f"Telefone: {client['phone']}")
