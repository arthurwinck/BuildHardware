from placa_mae import Placa_mae


def Escolher_Placa_mae():
    nome_do_componente = Placa_mae
    at1 = {'a1': "PotatoBoard 8000",
           'a2': 500,
           'a3': "1155",
           'a4': "DDR3",
           'a5': "Micro-ATX",
           'a6': 90}
    at2 = {'b1': "PotatoBoard 8000",
           'b2': 500,
           'b3': "1155",
           'b4': "DDR3",
           'b5': "Micro-ATX",
           'b6': 90}
    at3 = {'c1': "PotatoBoard 8000",
           'c2': 500,
           'c3': "1155",
           'c4': "DDR3",
           'c5': "Micro-ATX",
           'c6': 90}
    at4 = {'d1': "PotatoBoard 8000",
           'd2': 500,
           'd3': "1155",
           'd4': "DDR3",
           'd5': "Micro-ATX",
           'd6': 90}

    print('='*20, 'MotherBoards', '='*20)

        print('-'*20, f'{c}º Produto:', '-'*20)
        print(f'Modelo: {at1["a1"]}',
              f'Preço: R${at1["a2"]},00',
              f'Socket do Processador: {at1["a3"]}',
              f'Socket da Memória Ram: {at1["a4"]}',
              f'Tamanho da Placa Mãe: {at1["a5"]}',
              f'Voltagem consumida: {at1["a6"]}')
    componente1 = nome_do_componente(at1['a1'],
                                     at1['a2'],
                                     at1['a3'],
                                     at1['a4'],
                                     at1['a5'],
                                     at1['a6'])

batata = Escolher_Placa_mae()

