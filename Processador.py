def Escolher_Comp_Processador():
    name_at1 = 'Modelo'
    name_at2 = 'Preço'
    name_at3 = 'Socket'
    name_at4 = 'Voltagem Consumida'
    # de acordo com a quantidade de atributos

    atributo = [{name_at1: "DMA_Processor 100",
                 name_at2: 800,
                 name_at3: "AM3+",
                 name_at4: 140},
                {name_at1: "DMA_Processor 200",
                 name_at2: 500,
                 name_at3: "AM3+",
                 name_at4: 115},
                {name_at1: "LETNI_Processor 50",
                 name_at2: 1000,
                 name_at3: "1155",
                 name_at4: 110},
                {name_at1: "LETNI_Processor 250",
                 name_at2: 700,
                 name_at3: "1155",
                 name_at4: 90}]
    # de acordo com a quantidade de objetos

    contador = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto']  # de acordo com a quantidade de objetos
    contador2 = ['A', 'B', 'C', 'D']  # de acordo com a quantidade de objetos

    print ('=' * 20, 'Processor', '=' * 20)  # Alterar o nome do produto
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

    obj_processador = Comp_Processador (list[0], list[1], list[2], list[3])
    # Nome do Componente e de acordo com a quantidade de tributos

    return obj_processador  # Nome do Componente


class Comp_Processador:
    def __init__(self, modelo, preco, socket, voltagem):
        self.modelo = modelo
        self.preco = preco
        self.socket = socket
        self.voltagem = voltagem
