from tela_atletica import TelaAtletica
from atletica import Atletica



class ControladorAtletica():
    def __init__(self, controlador_sistema):
        self.__tela_atletica = TelaAtletica()
        self.__atleticas = []
        self.__controlador_sistema = controlador_sistema

    def pega_atletica_pelo_nome(self, nome: str):
        for atletica in self.__atleticas:
            if(atletica.nome == nome):
                return atletica
            return None


    def incluir_atletica(self):
        dados_atletica = self.__tela_atletica.pega_info_atletica()
        a = self.pega_atletica_pelo_nome(dados_atletica["Nome"])
        if a is None:
            atletica = Atletica(dados_atletica["curso"])
            self.__atleticas.append(atletica)
        else:
            self.__tela_atletica.mostra_mensagem("ATENCAO: Atletica já existente")

    def alterar_atletica(self):
        self.lista_atletica()
        codigo_livro = self.__tela_livro.seleciona_livro()
        livro = self.pega_livro_por_codigo(codigo_livro)

        if(livro is not None):
            novos_dados_livro = self.__tela_livro.pega_dados_livro()
            livro.titulo = novos_dados_livro["titulo"]
            livro.codigo = novos_dados_livro["codigo"]
            self.lista_livro()
        else:
            self.__tela_livro.mostra_mensagem("ATENCAO: Livro não existente")

  # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_livro(self):
    for livro in self.__livros:
      self.__tela_livro.mostra_livro({"titulo": livro.titulo, "codigo": livro.codigo})

  def excluir_livro(self):
    self.lista_livro()
    codigo_livro = self.__tela_livro.seleciona_livro()
    livro = self.pega_livro_por_codigo(codigo_livro)

    if(livro is not None):
      self.__livros.remove(livro)
      self.lista_livro()
    else:
      self.__tela_livro.mostra_mensagem("ATENCAO: Livro não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_livro, 2: self.alterar_livro, 3: self.lista_livro, 4: self.excluir_livro, 0: self.retornar}

    continua = True
    while continua:
      lista_opcoes[self.__tela_livro.tela_opcoes()]()