import Classes


def Escolher_Placa_mae():
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

    obj_placa_mae = Classes.Placa_mae (list[0], list[1], list[2], list[3], list[4], list[5])
    # Nome do componente e de acordo com a quantidade de tributos

    return obj_placa_mae  # Nome do Componente


def Escolher_Processador():
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

    obj_processador = Classes.Processador(list[0], list[1], list[2], list[3])
    # Nome do Componente e de acordo com a quantidade de tributos

    return obj_processador  # Nome do Componente


def Escolher_Processador_grafico():
    name_at1 = 'Modelo'
    name_at2 = 'Preço'
    name_at3 = 'Voltagem Consumida'
    # de acordo com a quantidade de atributos

    atributo = [{name_at1: "BG_Graphics",
                 name_at2: 800,
                 name_at3: 150},
                {name_at1: "ISM_Graphics",
                 name_at2: 500,
                 name_at3: 100}]
    # de acordo com a quantidade de objetos

    contador = ['Primeiro', 'Segundo']  # de acordo com a quantidade de objetos
    contador2 = ['A', 'B']  # de acordo com a quantidade de objetos

    print ('=' * 20, 'Processador Gráfico', '=' * 20)  # Alterar o nome do produto
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

    obj_processador_grafico = Classes.Processador_grafico (list[0], list[1], list[2])
    # Nome do Componente e de acordo com a quantidade de tributos

    return obj_processador_grafico  # Nome do Componente


def Escolher_Memoria_ram():
    name_at1 = 'Modelo'
    name_at2 = 'Preço'
    name_at3 = 'Socket'
    name_at4 = 'Voltagem Consumida'
    # de acordo com a quantidade de atributos

    atributo = [{name_at1: "Hyper_Ram_8GB",
                 name_at2: 200,
                 name_at3: "DDR3",
                 name_at4: 10},
                {name_at1: "Coug_Ram_16GB",
                 name_at2: 250,
                 name_at3: "DDR4",
                 name_at4: 15}]
    # de acordo com a quantidade de objetos

    contador = ['Primeiro', 'Segundo']  # de acordo com a quantidade de objetos
    contador2 = ['A', 'B']  # de acordo com a quantidade de objetos

    print ('=' * 20, 'Mémoria RAM', '=' * 20)  # Alterar o nome do produto
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

    obj_memoria_ram = Classes.Memoria_ram (list[0], list[1], list[2], list[3])
    # Nome do Componente e de acordo com a quantidade de tributos

    return obj_memoria_ram  # Nome do Componente


def Escolher_Fonte():
    name_at1 = 'Modelo'
    name_at2 = 'Preço'
    name_at3 = 'Watts'
    # de acordo com a quantidade de atributos

    atributo = [{name_at1: "AGVE_Energy",
                 name_at2: 400,
                 name_at3: 700},
                {name_at1: "Cors_Energy",
                 name_at2: 200,
                 name_at3: 400}]
    # de acordo com a quantidade de objetos

    contador = ['Primeiro', 'Segundo']  # de acordo com a quantidade de objetos
    contador2 = ['A', 'B']  # de acordo com a quantidade de objetos

    print ('=' * 20, 'Fonte', '=' * 20)  # Alterar o nome do produto
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

    obj_fonte = Classes.Fonte (list[0], list[1], list[2])
    # Nome do Componente e de acordo com a quantidade de tributos

    return obj_fonte  # Nome do Componente


def Escolher_Gabinete():
    name_at1 = 'Modelo'
    name_at2 = 'Preço'
    name_at3 = 'Socket da Placa Mãe'
    # de acordo com a quantidade de atributos

    atributo = [{name_at1: "KRASH_Cabinet",
                 name_at2: 250,
                 name_at3: "ATX"},
                {name_at1: "3C_Cabinet",
                 name_at2: 100,
                 name_at3: "Micro-ATX"}]
    # de acordo com a quantidade de objetos

    contador = ['Primeiro', 'Segundo']  # de acordo com a quantidade de objetos
    contador2 = ['A', 'B']  # de acordo com a quantidade de objetos

    print ('=' * 20, 'Gabinete', '=' * 20)  # Alterar o nome do produto
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

    obj_gabinete = Classes.Gabinete (list[0], list[1], list[2])
    # Nome do Componente e de acordo com a quantidade de tributos

    return obj_gabinete  # Nome do Componente


def Escolher_Armazenamento():
    name_at1 = 'Modelo'
    name_at2 = 'Preço'
    # de acordo com a quantidade de atributos

    atributo = [{name_at1: "SSD DiskSand 500 GB",
                 name_at2: 400},
                {name_at1: "HD GeatSea 2 TB",
                 name_at2: 200}]
    # de acordo com a quantidade de objetos

    contador = ['Primeiro', 'Segundo']  # de acordo com a quantidade de objetos
    contador2 = ['A', 'B']  # de acordo com a quantidade de objetos

    print ('=' * 20, 'Armazenamento', '=' * 20)  # Alterar o nome do produto
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

    obj_armazenamento = Classes.Armazenamento (list[0], list[1])
    # Nome do Componente e de acordo com a quantidade de tributos

    return obj_armazenamento  # Nome do Componente
