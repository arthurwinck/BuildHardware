import Classes
import Objetos


lista_clientes = []
lista_obj = []
lista_nome_build = []
lista_build = []


cont_obj = 0
cont_ver = 0
cont_ver_build = 0
cont_cadastro = 0
cont_mudanca = 0
cont_alterar_build = 0


while True:
    print('[A] Menu Clientes\n'
          '[B] Menu Computador\n'
          '[C] Finalizar\n'
          '[D] Ver Histórico do Último Comprado\n'
          '[E] Sair')

    menu_geral = input('Qual operação será efetuada ? [A/B/C/D]: ').upper()

    if menu_geral == 'A':

        while True:

            print('')
            print('[A] Cadastrar um Cliente\n'
            '[B] Alterar o Cadastro de um Cliente\n'
            '[C] Excluir o Cadastro de um Cliente\n'
            '[D] Imprimir os Cadastros dos Clientes\n'
            '[E] Voltar')
            print('')
            menu_clientes = input('Qual operação será efetuada ? [A/B/C/D]: ').upper()
            

            if menu_clientes == 'A':
                
                nome = input('Digite o Nome do Cliente: ').upper()
                cpf = int(input('Digite o CPF do Cliente: '))
                VIP = input('O Cliente possui VIP ? [S/N]: ').upper()

                for k in range(len(lista_clientes)):
                    for l in range(2):
                        if nome == lista_clientes[k][l]:
                            print("Dados inválidos, tente novamente")
                            
                            cont_cadastro = 1
                            
                        elif cpf == lista_clientes[k][l]:
                            print("Dados inválidos, tente novamente")
                                                      
                            cont_cadastro = 1
                    
                if cont_cadastro == 0:


                    if VIP == 'S':
                        lista_clientes.append([nome,cpf,'S'])
                        
                        
                        var = Classes.Cliente_VIP(nome, cpf, 'S')
                        
                        lista_obj.append(var)

                        ### INSTACIAÇÃO ###
                        cont_obj += 1
                        
                        print ('Processo Feito')
                           
                    if VIP == 'N':
                        lista_clientes.append([nome,cpf,'N'])

                        
                        var = Classes.Cliente_VIP(nome, cpf, 'N')
                        lista_obj.append(var)

                        ### INSTACIAÇÃO ###
                        cont_obj += 1
                

                        print ('Processo Feito')

                cont_cadastro = 0
                
                
                print(lista_clientes)

            if menu_clientes == 'B':
                    
                while True:
                    
                    print('')
                    print('[A] Mudar o nome')
                    print('[B] Mudar o cpf')
                    print('[C] Mudar o status do VIP')
                    print('[D] Voltar')
                    print('')

                    alt = str(input("O que você deseja fazer?")).upper()

                    if alt == 'D':
                        break

                    nome_alt = input('Digite o nome/cpf do Cliente a ser alterado: ').upper()
                
                    print(lista_clientes)

                    for a in range(len(lista_clientes)):
                        for b in range(2):

                            if nome_alt == lista_clientes[a][b]:
                                                           
                                var_obj = lista_obj[a]
                                cont_ver = 1
                                break
                    
                    if cont_ver == 0:
                            print()
                            print("Esse nome não foi encontrado, tente novamente.")
                            print()
                            
                    elif cont_ver == 1:            
                        if alt == 'A':

                            var_obj.alterar_cadastro(alt)
                            lista_clientes[a][0] = var_obj.nome

                            print()
                            print("nome mudado com sucesso!")
                            print()
                             

                        elif alt == 'B':
                                        
                            var_obj.alterar_cadastro(alt)
                            lista_clientes[a][1] = var_obj.cpf
                                        
                            print()
                            print("CPF mudado com sucesso!")
                            print()
                                  
                                            
                        elif alt == 'C':
                                        
                            var_obj.alterar_cadstro(alt)
                            lista_clientes[a][2] = var_obj.vip
                                        
                            print()
                            print("VIP mudado com sucesso!")
                            print()                 

                    cont_ver = 0

            if menu_clientes == "C":

                nome_del = str(input("Qual é o nome que você deseja exclcuir: ")).upper()

                for g in range(len(lista_clientes)):
                    
                    if lista_clientes[g][0] == nome_del:

                        var_del = lista_obj[g]
                        var_del.delete()

                        del lista_clientes[g]
                        del lista_obj[g]
                        del var_del
                
            if menu_clientes == "D":
                if len(lista_obj) == 0:
                    print("Não existem clientes para serem impressos!")
                else:
                    print()
                    var.imprimir(lista_clientes)
                    print()

            if menu_clientes == "E":
                break

    if menu_geral == 'B':
        
        while True:

            print('[A] Montar Build\n'
                  '[B] Excluir Build\n'
                  '[C] Voltar')
            
            menu_computador = input('Qual operação será efetuada ? [A/B/C]: ').upper()

            if menu_computador == 'A':

                nome_cliente = str(input('Qual o nome do Cliente a qual essa Build será montada?')).upper()
                nome_build = input('Digite o nome da Build a ser construida: ').upper()
                
                for d in range(len(lista_clientes)):
                        if nome_cliente == lista_clientes[d][0]:
                            print(f"Ok! Estamos montando a build para o/a {nome_cliente}")
                            cont_ver_build = 1

                lista_nome_build.append(nome_build)
                
                
                if cont_ver_build == 0:
                    print("Dados inválidos, tente novamente...")

                elif cont_ver_build == 1:
                    
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
                    
                   
                   print(Classes.Pecas.modelo)

                    lista_build.append(build)

            if menu_computador == "B":

                nome_build_excluir = input('Qual o nome da build que será excluída?').upper()
                
                for u in range(len(lista_nome_build)):
                    if nome_build_excluir == lista_nome_build[u]:
                        cont_alterar_build = 1
                        

                if cont_alterar_build == 0:
                    print("Não existe uma Build com esse nome, tente novamente.")

                elif cont_alterar_build == 1:
                    for h in range(len(lista_nome_build)):
                        if nome_build_excluir == lista_nome_build[h]:        
                            
                            nome_excluir = lista_obj[h]
                            
                            nome_excluir.__del__()

                           

                            lista_nome_build[h] = "Exclúido"
                            lista_build[h] = {'Placa mãe': "Excluído",
                                              'Processador': "Excluído",
                                              'Processador Gráfico': "Excluído",
                                              'Mémoria ram': "Excluído",
                                              'Fonte': "Excluído",
                                              'Gabinete': "Excluído",
                                              'Armazenamento': "Excluído"}

                            print(lista_nome_build)
                            print(lista_build)
                            print(lista_obj)
                            print(lista_clientes)

