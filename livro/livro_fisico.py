from livro.livro import Livro

class LivroFisico(Livro):
    def __init__(self, livro_id, autor, titulo, ano_publi, num_pag):
        super().__init__(livro_id, autor, titulo, ano_publi)
        self.__numero_paginas = num_pag

    @property
    def numero_paginas(self):
        return self.__numero_paginas

    @numero_paginas.setter
    def numero_paginas(self, value):
        self.__numero_paginas = value
