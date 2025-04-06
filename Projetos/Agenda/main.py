class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def editar(self, novo_nome, novo_telefone):
        self.nome = novo_nome
        self.telefone = novo_telefone

    def mostrar(self, idx):
        print(f"[{idx}] Nome: {self.nome}, Telefone: {self.telefone}")

class Agenda:
    def __init__(self):
        self.contatos = []

    def criar_contato(self):
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        self.contatos.append(Contato(nome, telefone))
        print("Contato adicionado!")

    def listar_contatos(self):
        if not self.contatos:
            print("Nenhum contato.")
            return
        for i, contato in enumerate(self.contatos):
            contato.mostrar(i)

    def editar_contato(self):
        self.listar_contatos()
        try:
            idx = int(input("ID do contato a editar: "))
            if idx < 0 or idx >= len(self.contatos):
                print("ID inválido.")
                return
            nome = input("Novo nome: ")
            telefone = input("Novo telefone: ")
            self.contatos[idx].editar(nome, telefone)
            print("Contato atualizado!")
        except ValueError:
            print("Entrada inválida.")

    def remover_contato(self):
        self.listar_contatos()
        try:
            idx = int(input("ID do contato a remover: "))
            if idx < 0 or idx >= len(self.contatos):
                print("ID inválido.")
                return
            del self.contatos[idx]
            print("Contato removido!")
        except ValueError:
            print("Entrada inválida.")

def menu():
    agenda = Agenda()
    while True:
        print("\n1. Criar\n2. Listar\n3. Editar\n4. Remover\n5. Sair")
        opcao = input("Escolha: ")

        if opcao == '1':
            agenda.criar_contato()
        elif opcao == '2':
            agenda.listar_contatos()
        elif opcao == '3':
            agenda.editar_contato()
        elif opcao == '4':
            agenda.remover_contato()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

menu()