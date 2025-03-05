from pymongo import MongoClient

# Criando classe mercadinho para melhor organização
class MercadinhoDB:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["Mercado"]

    def insere_item(self,colecao,item): #Insere item na coleção especificada
        self.db[colecao].insert_one(item)
        print(f"Item inserido na coleção: {colecao} : {item}")

    def listar_item(self,colecao): #Lista todos os itens da coleção
        return list(self.db[colecao].find())

    def remove_item(self,colecao,id_item): #Remove item de uma coleção pelo ID
        self.db[colecao].delete_one({"id": id_item})
        print(f"Item {id_item} removido da coleção {colecao}")
