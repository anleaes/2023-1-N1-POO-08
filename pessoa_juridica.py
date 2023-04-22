from pessoa import Pessoa

class PessoaJuridica(Pessoa):

    def __init__(self, nome, endereco, numero_de_telefone, cnpj , ano_de_fundacao):
        super().__init__(nome,  endereco, numero_de_telefone)
        self._cnpj = cnpj
        self._ano_de_fundacao = ano_de_fundacao