from database import Database
from motoristaDAO import MotoristaDAO
from motoristaCLI import MotoristaCLI

if __name__ == "__main__":
    database = Database("mongodb+srv://root:root@cluster0.lowsl.mongodb.net/")
    motorista_dao = MotoristaDAO(database)
    cli = MotoristaCLI(motorista_dao)
    cli.run()