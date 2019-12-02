import datetime
class Computador:
    def __init__(self):
        self.computador = []

    def imprimir_comp(self):
        print(self.computador)

    def __del__(self):
        print("Sua build foi exclúida")        


class Pecas:
    def __init__(self,modelo,preco):
        self.modelo = modelo
        self.preco = preco
        
        
class Placa_mae(Pecas):
    def __init__(self, modelo, preco, socket_processador, socket_memoria_ram, socket, voltagem):
    
        Pecas.__init__(self,modelo,preco)

        self.socket_processador = socket_processador
        self.socket_memoria_ram = socket_memoria_ram
        self.socket = socket
        self.voltagem = voltagem


class Processador(Pecas):
    def __init__(self, modelo, preco, socket, voltagem):

        Pecas.__init__(self,modelo,preco)

        self.modelo = modelo
        self.preco = preco
        self.socket = socket
        self.voltagem = voltagem


class Processador_grafico(Pecas):
    def __init__(self, modelo, preco, voltagem):

        Pecas.__init__(self,modelo,preco)

        self.voltagem = voltagem


class Memoria_ram(Pecas):
    def __init__(self, modelo, preco, socket, voltagem):

        Pecas.__init__(self,modelo,preco)

        self.socket = socket
        self.voltagem = voltagem


class Fonte(Pecas):
    def __init__(self, modelo, preco, watts):

        Pecas.__init__(self,modelo,preco)
    
        self.watts = watts


class Gabinete(Pecas):
    def __init__(self, modelo, preco, socket_placa_mae):

        Pecas.__init__(self,modelo,preco)

        self.socket_placa_mae = socket_placa_mae


class Armazenamento(Pecas):
    def __init__(self, modelo, preco):
        Pecas.__init__(self,modelo,preco)

################################# OUTRAS CLASSES ################################################

class Carrinho:
    def __init__(self,qtd_produtos,forma_pagamento, preco_total, preco_frete,pecas,cliente,data_abertura = datetime.datetime.today):
        self.qtd_produtos = 7
        self.forma_pagamento = forma_pagamento
        self.preco_total = pecas.preco
        self.preco_frete = preco_frete
        self.pecas = pecas.modelo
        self.cliente = cliente
        self.data_abertura = datetime.datetime.today

    def imprimir_carrinho(self):
        print(f'Preço do frete: {self.preco_frete}')
        print(f'forma de pagamento: {self.forma_pagamento}')
        
        for v in range(len(self.pecas)):
            print(f'Peças adquiridas: {self.pecas[v]}')
            print(f'Preço de cada peça: {self.preco_total[v]}')


    def metodo_pagamento(self, met_pag):
        if met_pag == 'A':
            self.forma_pagamento = 'Credito'
        elif met_pag == 'B':
            self.forma_pagamento = 'Débito'
        elif met_pag == 'C':
            self.forma_pagamento = 'Boleto'

    def var_frete(self, met_fret):
            if met_fret == 'A':
                self.preco_frete = 'Rápido = R$100,00'
            elif met_fret == 'B':
                self.preco_frete = 'Lento = R$50,00'
            elif met_fret == 'C':
                self.preco_frete = 'VIP = R$0,00'



class Cliente:
    def __init__(self, nome, cpf, vip):
        self.nome = nome
        self.cpf = cpf
        self.vip = vip

    def alterar_cadastro(self,alt):
        if alt == 'A':
            self.nome = str(input("Digite o novo nome: ")).upper()
        elif alt == 'B':
            self.cpf = int(input("Digite o novo cpf: "))
        elif alt == 'C':
            self.vip = str(input("Mude a condição do VIP [S]/[N]: ")).upper()

    def __del__(self):
        print("O cadastro foi excluído")

    def imprimir(self,clientes):
        print(clientes)


class Cliente_VIP (Cliente):
    def __init__(self, nome, cpf, vip):
        Cliente.__init__ (self, nome, cpf, vip)
        self.free_frete = 'Ativado'

