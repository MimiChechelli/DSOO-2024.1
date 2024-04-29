


class TelaAtletica():
    def tela_opcoes(self):
        print("-------- ATLETICA ----------")
        print("Escolha a opcao")
        print("1 - Incluir Atletica")
        print("2 - Alterar Atletica")
        print("3 - Listar Atletica")
        print("4 - Excluir Atletica")
        print("0 - Retornar")

        opcao = int(input("Escolha a opcao: "))
        return opcao
    
    def pega_info_atletica(self):
        print("-------- DADOS ATLETICA ----------")
        nome = input("Nome: ")
        curso = input("curso: ")
        alunos = input("alunos: ")
        return {"nome": nome, "curso": curso, "alunos": alunos}

    def mostra_atletica(self, dados_atletica):
        print("NOME DA ATLETICA: ", dados_atletica["nome"])
        print("CURSO DA ATLETICA: ", dados_atletica["curso"])
        print("ALUNOS DA ATLETICA: ", dados_atletica["alunos"])
        print("\n")

    def seleciona_atletica(self):
        nome = input("Nome da Atletica que deseja selecionar: ")
        return nome

    def mostra_mensagem(self, msg):
        print(msg)