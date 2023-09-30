from livro.livro import Livro
class LivroDigital(Livro):
    def __init__(self, livro_id, autor,titulo, ano_publi, formato):
        super().__init__(livro_id, autor,titulo, ano_publi)
        self.__formato = formato

    @property
    def formato(self):
        return self.__formato

    @formato.setter
    def formato(self, value):
        self.__formato = value


