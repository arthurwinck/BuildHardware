import Classes
import Objetos

cont_cadastro = 0
cont_mudanca = 0
lista_clientes = []

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
                    for l in range(3):
                        if nome == lista_clientes[k][l]:
                            print("Dados inválidos, tente novamente")
                            
                            cont_cadastro = 1
                            
                        elif cpf == lista_clientes[k][l]:
                            print("Dados inválidos, tente novamente")
                                                      
                            cont_cadastro = 1

                if cont_cadastro == 0:
                    if VIP == 'S':
                        lista_clientes.append([nome,cpf,'S'])
                        nome = Classes.Cliente_VIP(nome, cpf, 'S')

                        ### INSTACIAÇÃO ###

                        
                        print ('Processo Feito')
                           
                    if VIP == 'N':
                        lista_clientes.append([nome,cpf,'S'])
                        nome = Classes.Cliente_VIP(nome, cpf, 'S')

                        ### INSTACIAÇÃO ###

                        
                        print ('Processo Feito')

                cont_cadastro = 0
                
                print(lista_clientes)

            if menu_clientes == 'B':
                    
                while True:
                    
                    nome_alt = input('Digite o nome do Cliente a ser alterado: ').upper()

                    print('')
                    print('[A] Mudar o nome')
                    print('[B] Mudar o cpf')
                    print('[C] Mudar o status do VIP')
                    print('[D] Voltar')
                    print('')

                    alt = str(input("O que você deseja mudar?")).upper()

                    for a in range(len(lista_clientes)):
                        for b in range(3):

                            if nome_alt == lista_clientes[a][b]:
                                    
                                
                                if alt == 'A':
                                    
                                    Classes.Cliente.alterar_cadastro(nome_alt,lista_clientes[a][b],alt)
                                    print("nome mudado com sucesso!")
                                    cont_mudanca = 1

                                        

                                elif alt == 'B':
                                    cpf_mudar = int(input("Digite o novo número do CPF: "))
                                    lista_clientes[a][1] == cpf_mudar
                                    
                                    print()
                                    print("CPF mudado com sucesso!")
                                    print()

                                    cont_mudanca = 1

                                        

                                elif alt == 'C':
                                    vip_mudar = str(input("Mudar o VIP: [S/N] "))
                                    lista_clientes[a][2] == vip_mudar
                                    
                                    print()
                                    print("VIP mudado com sucesso!")
                                    print()

                                    cont_mudanca = 1

                                        

                                elif alt == 'D':
                                    break

                                    
                        if cont_mudanca == 0:
                            print()
                            print("Esse nome não foi encontrado, tente novamente.")
                            print()
                        elif cont_mudanca == 1:
                            print()
                            print("Alteração feita com sucesso!")
                            print()

                        cont_mudanca = 0
                    

                