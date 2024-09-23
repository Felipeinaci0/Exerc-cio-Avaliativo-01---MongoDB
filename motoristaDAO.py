class MotoristaDAO:
    def __init__(self, database):
        self.collection = database.get_collection('Motorista')

    def criar_motorista(self, motorista):
        self.collection.insert_one(motorista.__dict__)

    def ler_motorista(self, id_motorista):
        return self.collection.find_one({"_id": id_motorista})

    def atualizar_motorista(self, id_motorista, novos_dados):
        self.collection.update_one({"_id": id_motorista}, {"$set": novos_dados})

    def deletar_motorista(self, id_motorista):
        self.collection.delete_one({"_id": id_motorista})