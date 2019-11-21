def Escolher_Comp_Gabinete():
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

    obj_gabinete = Comp_Gabinete (list[0], list[1], list[2])
    # Nome do Componente e de acordo com a quantidade de tributos

    return obj_gabinete  # Nome do Componente


class Comp_Gabinete:
    def __init__(self, modelo, preco, socket_placa_mae):
        self.modelo = modelo
        self.preco = preco
        self.socket_placa_mae = socket_placa_mae

