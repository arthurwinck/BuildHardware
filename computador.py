from Placa_mae import Comp_Placa_mae, Escolher_Comp_Placa_mae
from Processador import Comp_Processador, Escolher_Comp_Processador
from Processador_grafico import Comp_Processador_grafico, Escolher_Comp_Processador_grafico
from Memoria_ram import Comp_Memoria_ram, Escolher_Comp_Memoria_ram
from Fonte import Comp_Fonte, Escolher_Comp_Fonte
from Gabinete import Comp_Gabinete, Escolher_Comp_Gabinete
from Armazenamento import Comp_Armazenamento, Escolher_Comp_Armazenamento


class Computador:
    def __init__(self, Comp_Placa_mae, Comp_Processador, Comp_Processador_grafico, Comp_Memoria_ram, Comp_Fonte,
                 Comp_Gabinete, Comp_Perifericos, Comp_Armazenamento):
        self.placa_mae = Comp_Placa_mae()
        self.processador = Comp_Processador()
        self.processador_grafico = Comp_Processador_grafico()
        self.memoria_ram = Comp_Memoria_ram()
        self.fonte = Comp_Fonte()
        self.gabinete = Comp_Gabinete()
        self.perifericos = Comp_Perifericos()
        self.armazenamento = Comp_Armazenamento()

    def Montar_Build(self):
        self.placa_mae = Escolher_Comp_Placa_mae()
        self.processador = Escolher_Comp_Processador()
        self.processador_grafico = Escolher_Comp_Processador_grafico()
        self.memoria_ram = Escolher_Comp_Memoria_ram()
        self.fonte = Escolher_Comp_Fonte()
        self.gabinete = Escolher_Comp_Gabinete()
        self.armazenamento = Escolher_Comp_Armazenamento()
