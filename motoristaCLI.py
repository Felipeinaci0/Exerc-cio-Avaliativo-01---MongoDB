class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")

class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_dao):
        super().__init__()
        self.motorista_dao = motorista_dao
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        nota = int(input("Nota do Motorista: "))
        motorista = Motorista(nota)
        
        num_corridas = int(input("Número de Corridas: "))
        for _ in range(num_corridas):
            nota_corrida = int(input("Nota da Corrida: "))
            distancia = float(input("Distância da Corrida: "))
            valor = float(input("Valor da Corrida: "))
            nome_passageiro = input("Nome do Passageiro: ")
            documento_passageiro = input("Documento do Passageiro: ")
            
            passageiro = Passageiro(nome_passageiro, documento_passageiro)
            corrida = Corrida(nota_corrida, distancia, valor, passageiro)
            motorista.adicionar_corrida(corrida)
        
        self.motorista_dao.criar_motorista(motorista)
        print("Motorista criado com sucesso!")

    def read_motorista(self):
        id_motorista = input("ID do Motorista: ")
        motorista = self.motorista_dao.ler_motorista(id_motorista)
        if motorista:
            print(motorista)
        else:
            print("Motorista não encontrado!")

    def update_motorista(self):
        id_motorista = input("ID do Motorista: ")
        novos_dados = {}
        nota = input("Nova nota do Motorista: ")
        if nota:
            novos_dados['nota'] = int(nota)
        
        if novos_dados:
            self.motorista_dao.atualizar_motorista(id_motorista, novos_dados)
            print("Motorista atualizado com sucesso!")
        else:
            print("Nenhum dado para atualizar!")

    def delete_motorista(self):
        id_motorista = input("ID do Motorista: ")
        self.motorista_dao.deletar_motorista(id_motorista)
        print("Motorista deletado com sucesso!")
        
    def run(self):
        print("Welcome to the Motorista CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()