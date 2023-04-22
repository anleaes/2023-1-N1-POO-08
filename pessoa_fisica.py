from pessoa import Pessoa

class PessoaFisica(Pessoa):

    def __init__(self, nome, endereco, numero_de_telefone, cpf, idade):
        super().__init__(nome,  endereco, numero_de_telefone)
        self._cpf = cpf
        self._idade = idade

        #print(isinstance(p1, Pessoa), isinstance(pf1, PessoaFisica))  testar hierarquia