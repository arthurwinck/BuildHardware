def Escolher_Comp_Fonte():
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

    obj_fonte = Comp_Fonte (list[0], list[1], list[2])
    # Nome do Componente e de acordo com a quantidade de tributos

    return obj_fonte  # Nome do Componente


class Comp_Fonte:
    def __init__(self, modelo, preco, watts):
        self.modelo = modelo
        self.preco = preco
        self.watts = watts

