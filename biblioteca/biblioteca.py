from livro.livro_fisico import LivroFisico
from membro.membro import Membro

class Biblioteca:
    def __init__(self):
        self.__livros =  []
        self.__membros = []

    def cadastrarMembro(self, membro: Membro):
        if membro in self.__membros:
            print("Usuário já cadastrado")
        else:
            self.__membros.append(membro)
            print("novo membro adicionado a biblioteca!")

    def deletarMembro(self, membro_id):
        for membro in self.__membros:
            if membro.membro_id == membro_id:
                self.__membros.remove(membro)
                print("Membro deletado com sucesso!")

    def deletarLivro(self, id):
        for livro in self.__livros:
            if livro.livro_id == id:
                self.__livros.remove(livro)
                print("livro deletado com sucesso!")
                
    def listarLivros(self):
        for livro in self.__livros:
            print(f"Id: {livro.livro_id}")
            print(f"Titulo: {livro.titulo}")
            print(f"Autor: {livro.autor}")
            print(f"Ano: {livro.ano_publi}")
            print(f"N de Paginas: {livro.numero_paginas} \n")
    
    def listarMembros(self):
        print("----- Membros Cadastrados -----")
        for membro in self.__membros:
            print(f"Id: {membro.membro_id}")
            print(f"Nome: {membro.nome}")
            print(f"Endereço: {membro.endereco}")
            print(F"telefone: {membro.telefone}")

    def cadastrarLivro(self, livro: LivroFisico):
        self.__livros.append(livro)
        print("livro adcionado com sucesso!")

if __name__ == "__main__":
    biblioteca = Biblioteca()  
    m1 = Membro(1, "luis", "Rua a", "88 99955-5555")
    m2 = Membro(2, "Carmem", "Rua c", "85 94754-5555")
    liv1 = LivroFisico(1, "tolkien", "LOR", 1970, 700)
    biblioteca.cadastrarMembro(m1)
    biblioteca.cadastrarMembro(m2)
    biblioteca.cadastrarLivro(liv1)
    biblioteca.listarMembros()
    biblioteca.listarLivros()