class Placa_mae:
    def __init__(self, modelo, preco, socket_processador, socket_memoria_ram, socket, voltagem):
        self.modelo = modelo
        self.preco = preco
        self.socket_processador = socket_processador
        self.socket_memoria_ram = socket_memoria_ram
        self.socket = socket
        self.voltagem = voltagem


class Processador:
    def __init__(self, modelo, preco, socket, voltagem):
        self.modelo = modelo
        self.preco = preco
        self.socket = socket
        self.voltagem = voltagem


class Processador_grafico:
    def __init__(self, modelo, preco, voltagem):
        self.modelo = modelo
        self.preco = preco
        self.voltagem = voltagem


class Memoria_ram:
    def __init__(self, modelo, preco, socket, voltagem):
        self.modelo = modelo
        self.preco = preco
        self.socket = socket
        self.voltagem = voltagem


class Fonte:
    def __init__(self, modelo, preco, watts):
        self.modelo = modelo
        self.preco = preco
        self.watts = watts


class Gabinete:
    def __init__(self, modelo, preco, socket_placa_mae):
        self.modelo = modelo
        self.preco = preco
        self.socket_placa_mae = socket_placa_mae


class Armazenamento:
    def __init__(self, modelo, preco):
        self.modelo = modelo
        self.preco = preco


class Pecas:
    def __init__(self, Placa_mae, Processador, Processador_grafico, Memoria_ram, Fonte, Gabinete, Armazenamento):
        self.Comp_Placa_mae = Placa_mae
        self.Comp_Processador = Processador
        self.Comp_Processador_grafico = Processador_grafico
        self.Comp_Memoria_ram = Memoria_ram
        self.Comp_Fonte = Fonte
        self.Comp_Gabinete = Gabinete
        self.Comp_Armazenamento = Armazenamento


class Historico:


class Carrinho:
    def __init__(self, qtd_produtos, forma_pagamento, preco_total, preco_frete):
        self.qtd_produtos = qtd_produtos
        self.forma_pagamento = forma_pagamento
        self.preco_total = preco_total
        self.preco_frete = preco_frete

    def qtd_produtos(self):
        self.qtd_produtos += 7

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

    def var_total(self):
        soma_preco =
        soma_frete =
        self.preco_total = soma_frete + soma_preco


class Cliente:
    def __init__(self, nome, cpf, vip):
        self.nome = nome
        self.cpf = cpf
        self.vip = vip


class Cliente_VIP (Cliente):
    def __init__(self, nome, cpf, vip):
        Cliente.__init__ (self, nome, cpf, vip)
        self.free_frete = 'Ativado'
