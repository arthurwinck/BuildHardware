import Classe from classe

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
    print("[A] Alterar o Cadastro de um Cliente")
    print("[B] Excluir o Cadastro de um Cliente")
    print("[C] Voltar")

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

elif menu == "B":

    menu_build = menu_build