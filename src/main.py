from db import MercadinhoDB

# Instanciando Mercadinho
mercado = MercadinhoDB()

# Inserindo um item no MongoDB
produto = {
    "id": 1,
    "nome": "Presunto",
    "preco_kg": 29.99,
    "validade": "2025-01-10"
}

mercado.insere_item("Frios",produto)

# Saida de dados
itens = mercado.listar_item("Frios")
print(itens)