

class Casa:
    def __init__(self, numero_casa: int, quartos: int, distancia: int, ar_condicionado: bool, diaria: float):
        self.numero_casa = numero_casa
        self.quartos = quartos
        self.distancia = distancia
        self.ar_condicionado = ar_condicionado
        self.diaria = diaria
        print(f"Casa {self.numero_casa} foi cadastrada!")
