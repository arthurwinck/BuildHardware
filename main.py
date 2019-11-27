import Objetos
import Classes

lista_clientes = []
nome_builds_montadas = []
builds_montadas = []
historico = []
contCad = 0
cont_verifica_nome = 0
cont_build = 0

while True:
    print('[A] Menu Clientes\n'
          '[B] Menu Computador\n'
          '[C] Finalizar\n'
          '[D] Ver Histórico do Último Comprado\n'
          '[E] Sair')
    menu_geral = input('Qual operação será efetuada ? [A/B/C/D]: ').upper()

    if menu_geral == 'A':

        while True:

            print('[A] Cadastrar um Cliente\n'
            '[B] Alterar o Cadastro de um Cliente\n'
            '[C] Excluir o Cadastro de um Cliente\n'
            '[D] Imprimir os Cadastros dos Clientes\n'
            '[E] Voltar')
            menu_clientes = input('Qual operação será efetuada ? [A/B/C/D]: ').upper()
            

            if menu_clientes == 'A':

                nome = input('Digite o Nome do Cliente: ').upper()
                cpf = int(input('Digite o CPF do Cliente: '))
                VIP = input('O Cliente possui VIP ? [S/N]: ').upper()

                for k in range(len(lista_clientes)):
                    for l in range(3):
                        if nome == lista_clientes[k][l]:
                            print("Dados inválidos, tente novamente")
                            contCad = 1
                            break
                        elif cpf == lista_clientes[k][l]:
                            print("Dados inválidos, tente novamente")
                            contCad = 1
                            break                        

                if contCad == 0:
                    if VIP == 'S':
                        nome_classe = nome
                        nome_classe = Classes.Cliente_VIP(nome, cpf, 1)
                        lista_clientes.append([nome,cpf,1])
                        print(lista_clientes)
                    if VIP == 'N':
                        nome = Classes.Cliente_VIP(nome, cpf, 0)
                        lista_clientes.append([nome,cpf,0])

                    print ('Processo Feito')

                
                    
                

            if menu_clientes == 'B':
    
                while True:
                    nome_alt = input('Digite o nome do Cliente a ser alterado: ').upper()
                    alt = int(input("Digite: 1-Mudar o nome\n2-Mudar o cpf\n3-Mudar o status do VIP\n4-Voltar"))

                    for a in range(len(lista_clientes)):
                        for b in range(3):
                            if nome_alt == lista_clientes[a][b]:
                                
                                if alt == 1:
                                    nome_mudar = str(input("Digite o novo nome: ")).upper()
                                    lista_clientes[a][b] == nome_mudar
                                    print("nome mudado com sucesso!")
                                elif alt == 2:
                                    cpf_mudar = int(input("Digite o novo número do CPF: "))
                                    lista_clientes[a][1] == cpf_mudar
                                    print("CPF mudado com sucesso!")
                                elif alt == 3:
                                    vip_mudar = int(input("Mudar para: 1-Ganhar o VIP\n0-Perder o VIP"))
                                    lista_clientes[a][2] == vip_mudar
                                    print("VIP mudado com sucesso!")
                                elif alt == 4:
                                    break

                    
                    mudar = str(input("Deseja mudar mais alguma coisa? 1-Sim\n 2-Não"))
                    if mudar == 2:
                        break

            
            

            if menu_clientes == 'C':
                nome_exc = str(input('Digite o nome do Cliente a ser excluido: ')).upper()

                while True:
                    for o in range(len(lista_clientes)):
                            for t in range(3):
                                if nome_exc == lista_clientes[o][t]:
                                    del lista_clientes[o]
                                    print("Nome excluído com sucesso!")
                                else:
                                    print("Nome não encontrado")
                    
                    excluir = int(input("Nome não encontrado, deseja tentar novamente? 1-Sim\n2-Não"))

                    if excluir == 2:
                        break
                        
            if menu_clientes == 'D':
                print(lista_clientes)
                

            if menu_clientes == 'E':
                break

    ######################################################### MENU BUILD ############################################################

    if menu_geral == 'B':
        
        while True:

            print('[A] Montar Computador\n'
                '[B] Excluir Componente\n'
                '[C] Voltar')
            menu_computador = input('Qual operação será efetuada ? [A/B/C]: ').upper()

            if menu_computador == 'A':

                nome_build = input('Digite o nome da Build a ser construida: ').upper()
                nome_cliente = str(input('Qual o nome do Cliente a qual essa Build será montada?')).upper()
                
                for x in range(len(lista_clientes)):
                    for y in range(3):
                        if nome == lista_clientes[x][y]:
                                print("Dados inválidos, tente novamente")
                                cont_verifica_nome = 1
                                break

                if cont_verifica_nome == 0:
                    print("Esse cliente não está cadastrado ainda!")
                    break    

                obj_Placa_mae = Objetos.Escolher_Placa_mae()
                obj_Processador = Objetos.Escolher_Processador()
                obj_Processador_grafico = Objetos.Escolher_Processador_grafico()
                obj_Memoria_ram = Objetos.Escolher_Memoria_ram()
                obj_Fonte = Objetos.Escolher_Fonte()
                obj_Gabinete = Objetos.Escolher_Gabinete()
                obj_Armazenamento = Objetos.Escolher_Armazenamento()


                build = {'Placa mãe': obj_Placa_mae,
                        'Processador': obj_Processador,
                        'Processador Gráfico': obj_Processador_grafico,
                        'Mémoria ram': obj_Memoria_ram,
                        'Fonte': obj_Fonte,
                        'Gabinete': obj_Gabinete,
                        'Armazenamento': obj_Armazenamento}

                nome_builds_montadas.append(nome_build)
                builds_montadas.append(build)
                
                #### INSTANCIAÇÃO ####

                nome_Placa_mae = obj_Placa_mae[0]
                nome_Placa_mae = Classes.Placa_mae(obj_Placa_mae[0],obj_Placa_mae[1],obj_Placa_mae[2],obj_Placa_mae[3],obj_Placa_mae[4],obj_Placa_mae[5])

                nome_Processador = obj_Processador[0]
                nome_Processador = Classes.Processador(obj_Processador[0],obj_Processador[1],obj_Processador[2],obj_Processador[3])

                nome_Processador_grafico = obj_Processador_grafico[0]
                nome_Processador_grafico = Classes.Processador_grafico(obj_Processador_grafico[0],obj_Processador_grafico[1],obj_Processador_grafico[2])

                nome_Memoria_ram = obj_Memoria_ram[0]
                nome_Memoria_ram = Classes.Memoria_ram(obj_Memoria_ram[0],obj_Memoria_ram[0],obj_Memoria_ram[0],obj_Memoria_ram[0])

                nome_Fonte = obj_Fonte[0]
                nome_Fonte = Classes.Fonte(obj_Fonte[0],obj_Fonte[1],obj_Fonte[2])

                nome_Armazenamento = obj_Armazenamento[0]
                nome_Armazento = Classes.Armazenamento(obj_Armazenamento[0],obj_Armazenamento[1],)

                cont_build += 1
                
                print('Computador Montado')

            if menu_computador == 'B':
                
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
                    
                elif comp_alt == 'B':
                    obj_Processador = Objetos.Escolher_Processador ()
                    build_alterada['Processador'] = obj_Processador
                    print ('Alterado com Sucesso !!!')
                    
                elif comp_alt == 'C':
                    obj_Processador_grafico = Objetos.Escolher_Processador_grafico ()
                    build_alterada['Processador Gráfico'] = obj_Processador_grafico
                    print ('Alterado com Sucesso !!!')
                    
                elif comp_alt == 'D':
                    obj_Memoria_ram = Objetos.Escolher_Memoria_ram ()
                    build_alterada['Mémoria ram'] = obj_Memoria_ram
                    print ('Alterado com Sucesso !!!')
                    
                elif comp_alt == 'E':
                    obj_Fonte = Objetos.Escolher_Fonte ()
                    build_alterada['Fonte'] = obj_Fonte
                    print ('Alterado com Sucesso !!!')
                    
                elif comp_alt == 'F':
                    obj_Gabinete = Objetos.Escolher_Gabinete ()
                    build_alterada['Gabinete'] = obj_Gabinete
                    print ('Alterado com Sucesso !!!')
                    
                elif comp_alt == 'G':
                    obj_Armazenamento = Objetos.Escolher_Armazenamento ()
                    build_alterada['Armazenamento'] = obj_Armazenamento
                    print ('Alterado com Sucesso !!!')
                    
                else:
                    break

                builds_montadas[posi3] = build_alterada



            if menu_computador == 'C':
                print("dale")
                break

    if menu_geral == "C":
        if cont_build >= 1:
            qtd_produtos = 7
            met_pag = str(input("Como você deseja pagar A - Crédito\nB - Débito\nC- Boleto"))
            
            if VIP == 1:
                met_fret = "C"
            else:
                met_fret = input("Qual frete você deseja? A - Normal - R$100\nB - Rápido - R$50")
            
            preco_frete = met_pag
            preco_total = 100
            forma_pagamento = met_fret
            
            for u in range(len(lista_clientes)):
                for f in range(3):
                    if nome_cliente == lista_clientes[u][f]:
                        nome_cliente = Classes.Cliente(nome_cliente,lista_clientes[u][1],lista_clientes[u][2])


            pecas = Classes.Pecas([obj_Placa_mae[0],obj_Processador[0],obj_Processador_grafico[0],obj_Memoria_ram[0],obj_Fonte[0],obj_Armazenamento[0]],[obj_Placa_mae[1],obj_Processador[1],obj_Processador_grafico[1],obj_Memoria_ram[1],obj_Fonte[1],obj_Armazenamento[1]])
            

            Carrinho1 = Classes.Carrinho(qtd_produtos,forma_pagamento,pecas,preco_frete,pecas,nome_cliente)

           

            cont_build =- 1

            print("Parabéns, você acaba de montar um computador!")
        else:
            print("Você não montou um computador para finalizar o seu carrinho!")

    if menu_geral == "D":
        Classes.Carrinho.imprimir_carrinho(Carrinho1)
    
    if menu_geral == "E":
        break   







