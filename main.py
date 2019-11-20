from Cliente import cliente

def menu():
    print("[A] Menu Clientes")
    print("[B] Menu Computador")
    print("[C] Fechar Compra")
    print("[D] Sair")

    menu = str(input("O que você deseja fazer?")).upper()
    while menu != "A" and menu != "B" and menu != "C" and menu != "D":
        print("Dados inválidos")
        menu = str(input("O que você deseja fazer?")).upper()
    return menu

def menu_cliente():
    print("[A] Cadastrar de um Cliente")
    print("[B] Alterar o Cadastro de um Cliente")
    print("[C] Excluir o Cadastro de um Cliente")
    print("[D] Voltar")

    menu_cliente = str(input("O que você deseja fazer")).upper()
    while menu != "A" and menu != "B" and menu != "C":
        print("Dados inválidos")
        menu_cliente = str(input("O que você deseja fazer?")).upper()

    return menu_cliente

def menu_build():
    print("[A] Começar a Build")
    print("[B] Excluir Componente")

    menu_build = str(input("O que você deseja fazer?")).upper()
    while menu_build != "A" and menu_build != "B":
        print("Dados inválidos")
        menu_build = str(input("O que você deseja fazer?")).upper()
        
    return menu_build

menu = menu()

if menu == "A":
    
    menu_cliente = menu_cliente()

    if menu_cliente == "A":
        nome = str(input("Escreva o nome do cliente: "))
        cpf = str(input("Escreva o CPF: "))
        novo_cliente = Cliente(nome,cpf)
    
    elif menu_cliente = "B":
        change = str(input("O que você quer mudar?"))
            


elif menu == "B":

    menu_build = menu_build()

    if menu_build == "A":
        nome_build = str(input("Escreva o nome da Build: "))
        nome_build = Computador()
        lista_build.append(nome_build)
        
    if menu_build == "B":

    