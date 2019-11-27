
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

while True
op1 = Menu_Geral()

if op1 == 'A':
    op2 = Menu_Clientes()
    

    if op2 == 'A':

        nome = input ('Digite o Nome do Cliente: ').upper ()
        cpf = int (input ('Digite o CPF do Cliente: '))

        if nome in lista_clientes or cpf in lista_clientes:
            print("Dados inválidos, já existe um cliente com esse nome/cpf")
        else:
            VIP = input('O Cliente possui VIP ? [S/N]: ').upper()
            if VIP == 'S':
                lista_clientes.append(Classes.Cliente_VIP([nome, cpf, 1]))
            if VIP == 'N':
                lista_clientes.append(Classes.Cliente([nome, cpf, 0]))
            print ('Processo Feito')
            op2 = Menu_Clientes()
        op2 = Menu_Clientes()

    if op2 == 'B':
        
        while True:

            nome_alt = str(input("Digite o nome a ser alterado")),upper()

            for a in range(len(lista_clientes)):
                for b in range(3):
                    if nome_alt == lista_clientes[a][b]:
                        alt = int(input("Digite: A-Mudar o nome\nB-Mudar o cpf\nC-Mudar o status do VIP")
                         
                        if alt == 'A':
                            nome_mudar = str(input("Digite o novo nome: "))
                            lista_clientes[a][b] == nome_mudar
                            print("nome mudado com sucesso!")
                        elif alt == 'B':
                            cpf_mudar = int(input("Digite o novo número do CPF: "))
                            lista_clientes[a][1] == cpf_mudar:
                            print("CPF mudado com sucesso!")
                        elif alt == 'C':
                            vip_mudar = int(input("Mudar para: 1-Ganhar o VIP\n0-Perder o VIP"))
                            lista_clientes[a][2] == vip_mudar
                            print("VIP mudado com sucesso!")

            mudar = str(input("Deseja mudar mais alguma coisa? 1-Sim\n 2-Não"))
            if mudar == 2:
                break

        print('Processo Feito')
        op2 = Menu_Clientes()

    if op2 == 'C':
        nome_exc = str(input('Digite o nome do Cliente a ser excluido: ').upper ()

        while True:
            for a in range(len(lista_clientes)):
                    for b in range(3):
                        if nome_exc == lista_clientes[a][b]:
                            del lista_clientes[a]
                            print("Nome excluído com sucesso!")
                        else:
                            print("Nome não encontrado")
            
            excluir = int(input("Nome não encontrado, deseja tentar novamente? 1-Sim\n2-Não")

            if excluir == 2:
                break
                    
        op2 = Menu_Clientes ()