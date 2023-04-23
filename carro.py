<<<<<<< HEAD
from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, preco, cor, placa):
        super().__init__(marca, modelo, ano, preco)
        self.cor = cor
        self.placa = placa
=======
class Carro:
    def __init__(self, marca, ano, tipo):
        self.marca = marca
        self.ano = ano
        self.tipo = tipo
>>>>>>> d9d0dc94a7284e7cac2c9c2f98a7cc7fb7cd2b8d
