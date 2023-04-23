class Concessionaria:
<<<<<<< HEAD
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.vendedores = []
        self.estoque = []

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"{cliente.nome} registrado como cliente da concessionária.")

    def registrar_vendedor(self, vendedor):
        self.vendedores.append(vendedor)
        print(f"{vendedor.nome} registrado como vendedor da concessionária.")

    def adicionar_carro_ao_estoque(self, carro):
        self.estoque.append(carro)
        print(f"O carro: {carro.modelo} {carro.marca} foi adicionado ao estoque.")

    def listar_carros_em_estoque(self):
        if len(self.estoque) == 0:
            print("Não há carros em estoque.")
        else:
            print("Carros em estoque:")
            for carro in self.estoque:
                print(f"{carro.modelo} {carro.marca} - {carro.ano}")

    def listar_clientes(self):
        if len(self.clientes) == 0:
            print("Não há clientes registrados.")
        else:
            print("Clientes registrados:")
            for cliente in self.clientes:
                print(cliente.nome)

    def listar_vendedores(self):
        if len(self.vendedores) == 0:
            print("Não há vendedores registrados.")
        else:
            print("Vendedores registrados:")
            for vendedor in self.vendedores:
                print(vendedor.nome)

    def encontrar_carro_por_modelo(self, modelo):
        for carro in self.estoque:
            if carro.modelo == modelo:
                return carro
        print(f"Não foi encontrado nenhum carro do modelo {modelo} em estoque.")
        return None

    def encontrar_vendedor_por_nome(self, nome):
        for vendedor in self.vendedores:
            if vendedor.nome == nome:
                return vendedor
        print(f"Não foi encontrado nenhum vendedor com o nome {nome}.")
=======
    
    def __init__(self, endereco, cnpj, numero_da_concessionaria, carro, moto, pessoa):
        self._endereco = endereco
        self._cnpj = cnpj
        self._numero_da_concessionaria = numero_da_concessionaria
        self._carro = carro
        self._moto - moto
        self._pessoa = pessoa
>>>>>>> d9d0dc94a7284e7cac2c9c2f98a7cc7fb7cd2b8d
