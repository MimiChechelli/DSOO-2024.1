

class Cliente:
    def __init__(self, nome, historico):
        self.nome = nome
        self.historico = historico
        print(f"{self.nome} foi cadastrado com sucesso!")
