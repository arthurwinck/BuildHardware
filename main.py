import Objetos
import Classes

lista_clientes = []
nome_builds_montadas = []
builds_montadas = []
historico = []


def Menu_Geral():
    print('[A] Menu Clientes\n'
          '[B] Menu Computador\n'
          '[C] Finalizar Compra\n'
          '[D] Sair')
    menu_geral = input('Qual operação será efetuada ? [A/B/C/D]: ').upper()
    return menu_geral


def Menu_Clientes():
    print('[A] Cadastrar um Cliente\n'
          '[B] Alterar o Cadastro de um Cliente\n'
          '[C] Excluir o Cadastro de um Cliente\n'
          '[D] Voltar')
    menu_clientes = input('Qual operação será efetuada ? [A/B/C/D]: ').upper()
    return menu_clientes


def Menu_Computador():
    print('[A] Montar Computador\n'
          '[B] Excluir Componente\n'
          '[C] Voltar')
    menu_computador = input('Qual operação será efetuada ? [A/B/C]: ').upper()
    return menu_computador


def Menu_Compra():
    print('[A] ')


op1 = Menu_Geral()

if op1 == 'A':
    op2 = Menu_Clientes()
    nome = input ('Digite o Nome do Cliente: ').upper ()
    cpf = int (input ('Digite o CPF do Cliente: '))

    if op2 == 'A':
        VIP = input('O Cliente possui VIP ? [S/N]: ').upper()
        if VIP == 'S':
            lista_clientes.append(Classes.Cliente_VIP(nome, cpf, 1))
        if VIP == 'N':
            lista_clientes.append(Classes.Cliente(nome, cpf, 0))
        print ('Processo Feito')
        op2 = Menu_Clientes()

    if op2 == 'B':
        nome_alt = input('Digite o nome do Cliente a ser alterado: ').upper()
        posi1 = lista_clientes.index(nome_alt)
        del lista_clientes[posi1]
        print('Digite os novos Dados do Cliente: ')
        VIP = input('O Cliente possui VIP ? [S/N]: ').upper()
        if VIP == 'S':
            lista_clientes.append(Classes.Cliente_VIP(nome, cpf, 1))
        if VIP == 'N':
            lista_clientes.append(Classes.Cliente(nome, cpf, 0))
        print('Processo Feito')
        op2 = Menu_Clientes()

    if op2 == 'C':
        nome_exc = input ('Digite o nome do Cliente a ser excluido: ').upper ()
        posi2 = lista_clientes.index(nome_exc)
        del lista_clientes[posi2]
        print ('Processo Feito')
        op2 = Menu_Clientes ()

    if op2 == 'D':
        op1 = Menu_Geral()

if op1 == 'B':
    op3 = Menu_Computador()

    if op3 == 'A':
        nome_build = input('Digite o nome da Build a ser construida: ').upper()
        nome_cliente = input('Qual o nome do Cliente a qual essa Build será montada? \nCaso não foi cadastrado ainda, favor digitar [0] para cadastra-lo !!!').upper()
        if nome_cliente == '0':
            op1 = Menu_Geral()

        obj_Placa_mae = Objetos.Escolher_Placa_mae ()
        obj_Processador = Objetos.Escolher_Processador ()
        obj_Processador_grafico = Objetos.Escolher_Processador_grafico ()
        obj_Memoria_ram = Objetos.Escolher_Memoria_ram ()
        obj_Fonte = Objetos.Escolher_Fonte ()
        obj_Gabinete = Objetos.Escolher_Gabinete ()
        obj_Armazenamento = Objetos.Escolher_Armazenamento ()

        obj_Comp_Placa_mae = Classes.Pecas(obj_Placa_mae,
                                           obj_Processador,
                                           obj_Processador_grafico,
                                           obj_Memoria_ram,
                                           obj_Fonte,
                                           obj_Gabinete,
                                           obj_Armazenamento)

        build = {'Placa mãe': obj_Placa_mae,
                 'Processador': obj_Processador,
                 'Processador Gráfico': obj_Processador_grafico,
                 'Mémoria ram': obj_Memoria_ram,
                 'Fonte': obj_Fonte,
                 'Gabinete': obj_Gabinete,
                 'Armazenamento': obj_Armazenamento}

        nome_builds_montadas.append(nome_build)
        builds_montadas.append(build)
        print('Computador Montado')
        op3 = Menu_Computador()

    if op3 == 'B':
        nome_build_alterada = input('Qual o nome da build que o componente será alterado?').upper()
        posi3 = nome_builds_montadas.index(nome_build_alterada)
        build_alterada = builds_montadas[posi3]
        builds_montadas[posi3] = 'Em Manutenção'

        print('Componentes que podem ser alterados:\n'
              '[A] Placa Mãe\n'
              '[B] Processador\n'
              '[C] Processador Gráfico\n'
              '[D] Mémoria Ram\n'
              '[E] Fonte\n'
              '[F] Gabinete\n'
              '[G] Armazenamento')

        comp_alt = input('Qual Componente você quer alterar?: ').upper()

        if comp_alt == 'A':
            obj_Placa_mae = Objetos.Escolher_Placa_mae ()
            build_alterada['Placa mãe'] = obj_Placa_mae
            print('Alterado com Sucesso !!!')
            op3 = Menu_Computador()
        elif comp_alt == 'B':
            obj_Processador = Objetos.Escolher_Processador ()
            build_alterada['Processador'] = obj_Processador
            print ('Alterado com Sucesso !!!')
            op3 = Menu_Computador ()
        elif comp_alt == 'C':
            obj_Processador_grafico = Objetos.Escolher_Processador_grafico ()
            build_alterada['Processador Gráfico'] = obj_Processador_grafico
            print ('Alterado com Sucesso !!!')
            op3 = Menu_Computador ()
        elif comp_alt == 'D':
            obj_Memoria_ram = Objetos.Escolher_Memoria_ram ()
            build_alterada['Mémoria ram'] = obj_Memoria_ram
            print ('Alterado com Sucesso !!!')
            op3 = Menu_Computador ()
        elif comp_alt == 'E':
            obj_Fonte = Objetos.Escolher_Fonte ()
            build_alterada['Fonte'] = obj_Fonte
            print ('Alterado com Sucesso !!!')
            op3 = Menu_Computador ()
        elif comp_alt == 'F':
            obj_Gabinete = Objetos.Escolher_Gabinete ()
            build_alterada['Gabinete'] = obj_Gabinete
            print ('Alterado com Sucesso !!!')
            op3 = Menu_Computador ()
        elif comp_alt == 'G':
            obj_Armazenamento = Objetos.Escolher_Armazenamento ()
            build_alterada['Armazenamento'] = obj_Armazenamento
            print ('Alterado com Sucesso !!!')
            op3 = Menu_Computador ()
        else:
            op3 = Menu_Computador()

        builds_montadas[posi3] = build_alterada

    if op3 == 'C':
        op1 = Menu_Geral()









