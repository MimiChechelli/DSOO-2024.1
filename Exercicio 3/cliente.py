


class Cliente:
    def __init__(self, nome: str, fone: int):
        self.__nome = None
        self.__fone = None

        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(fone, int):
            self.__fone = fone

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def fone(self):
        return self.__fone
    
    @fone.setter
    def fone(self, fone: int):
        if isinstance(fone, int):
            self.__fone = fone

