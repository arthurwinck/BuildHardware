def Escolher_Comp_Placa_mae():
    name_at1 = 'Modelo'
    name_at2 = 'Preço'
    name_at3 = 'Socket do Processador'
    name_at4 = 'Socket da Memória RAM'
    name_at5 = 'Tamanho da Placa Mãe'
    name_at6 = 'Voltagem Consumida'
    # de acordo com a quantidade de atributos

    atributo = [{name_at1: "PotatoBoard 8000",
                 name_at2: 500,
                 name_at3: "1155",
                 name_at4: "DDR3",
                 name_at5: "Micro-ATX",
                 name_at6: 90},
                {name_at1: "TomatoBoard 9000",
                 name_at2: 450,
                 name_at3: "AM3+",
                 name_at4: "DDR4",
                 name_at5: "ATX",
                 name_at6: 80},
                {name_at1: "PepinoBoard 7000",
                 name_at2: 350,
                 name_at3: "1155",
                 name_at4: "DDR3",
                 name_at5: "Micro-ATX",
                 name_at6: 70},
                {name_at1: "SpinachBoard 6000",
                 name_at2: 300,
                 name_at3: "AM3+",
                 name_at4: "DDR4",
                 name_at5: "ATX",
                 name_at6: 50}]
    # de acordo com a quantidade de objetos

    contador = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto']  # de acordo com a quantidade de objetos
    contador2 = ['A', 'B', 'C', 'D']  # de acordo com a quantidade de objetos

    print ('=' * 20, 'MotherBoards', '=' * 20)
    c = 0
    for n in atributo:
        print ('-' * 15, f'{contador[c]} Produto: [{contador2[c]}] ', '-' * 15)
        for k, v in n.items ():
            print (f'{k}: {v}')
        c += 1
    print ('=' * 52)

    while True:
        res = input (f'Qual modelo você quer adicionar{contador2}: ').upper ()
        if res in contador2:
            break
        else:
            print ('-' * 15)
            print ('Modelo Invalido !!!\n'
                   'Tente Outro Modelo')
            print ('-' * 15)
    print ('=' * 52)

    posi = contador2.index (res)
    list = []
    for k in atributo[posi].values ():
        list.append (k)

    obj_placa_mae = Comp_Placa_mae (list[0], list[1], list[2], list[3], list[4], list[5])
    # Nome do componente e de acordo com a quantidade de tributos

    return obj_placa_mae  # Nome do Componente


class Comp_Placa_mae:
    def __init__(self, modelo, preco, socket_processador, socket_memoria_ram, socket, voltagem):
        self.modelo = modelo
        self.preco = preco
        self.socket_processador = socket_processador
        self.socket_memoria_ram = socket_memoria_ram
        self.socket = socket
        self.voltagem = voltagem
