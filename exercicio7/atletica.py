


class Atletica():
    def __init__(self, curso: str, nome: str):
        self.__curso = curso
        self.__nome = nome
        self.__alunos = []
    
    @property
    def curso(self):
        return self.__curso
    
    @curso.setter
    def curso(self, curso):
        self.__curso = curso
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def alunos(self):
        return self.__alunos
    
    @alunos.setter
    def alunos(self, alunos):
        self.__alunos = alunos
