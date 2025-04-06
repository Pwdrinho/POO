agenda = []

def criar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    agenda.append({"nome": nome, "telefone": telefone})
    print("Contato adicionado!")

def listar_contatos():
    if not agenda:
        print("Nenhum contato.")
        return
    for i, contato in enumerate(agenda):
        print(f"[{i}] Nome: {contato['nome']}, Telefone: {contato['telefone']}")

def editar_contato():
    listar_contatos()
    try:
        idx = int(input("ID do contato a editar: "))
        if idx < 0 or idx >= len(agenda):
            print("ID inválido.")
            return
        nome = input("Novo nome: ")
        telefone = input("Novo telefone: ")
        agenda[idx] = {"nome": nome, "telefone": telefone}
        print("Contato atualizado!")
    except ValueError:
        print("Entrada inválida.")

def remover_contato():
    listar_contatos()
    try:
        idx = int(input("ID do contato a remover: "))
        if idx < 0 or idx >= len(agenda):
            print("ID inválido.")
            return
        del agenda[idx]
        print("Contato removido!")
    except ValueError:
        print("Entrada inválida.")

def menu():
    print("\n--- Agenda ---")
    while True:
        print("\n1. Criar\n2. Listar\n3. Editar\n4. Remover\n5. Sair")
        opcao = input("Escolha: ")

        if opcao == '1':
            criar_contato()
        elif opcao == '2':
            listar_contatos()
        elif opcao == '3':
            editar_contato()
        elif opcao == '4':
            remover_contato()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

menu()
