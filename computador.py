from Placa_mae import Comp_Placa_mae
from Processador import Comp_Processador
from Processador_grafico import Comp_Processador_grafico
from Memoria_ram import Comp_Memoria_ram
from Fonte import Comp_Fonte
from Gabinete import Comp_Gabinete
from Perifericos import Comp_Perifericos
from Armazenamento import Comp_Armazenamento


class Computador:
    def __init__(self):
        self.placa_mae = Comp_Placa_mae()
        self.processador = Comp_Processador()
        self.processador_grafico = Comp_Processador_grafico()
        self.memoria_ram = Comp_Memoria_ram()
        self.fonte = Comp_Fonte()
        self.gabinete = Comp_Gabinete()
        self.perifericos = Comp_Perifericos()
        self.armazenamento = Comp_Armazenamento()
