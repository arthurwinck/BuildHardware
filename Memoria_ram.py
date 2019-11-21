def Escolher_Comp_Memoria_ram():
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

    obj_memoria_ram = Comp_Memoria_ram (list[0], list[1], list[2], list[3])
    # Nome do Componente e de acordo com a quantidade de tributos

    return obj_memoria_ram  # Nome do Componente


class Comp_Memoria_ram:
    def __init__(self, modelo, preco, socket, voltagem):
        self.modelo = modelo
        self.preco = preco
        self.socket = socket
        self.voltagem = voltagem

