class Contato: 
    def __init__(self, nome, telefone): 
        self.nome = nome 
        self.telefone = telefone

    def __str__(self):
        return f"{self.nome}: {self.telefone}"

class Agenda: 
    def __init__(self): 
        self.contatos = []

    def adicionar_contato(self, nome, telefone):
        self.contatos.append(Contato(nome, telefone))
        print("Contato adicionado com sucesso!")

    def listar_contatos(self):
        if not self.contatos:
            print("A agenda está vazia.")
        else:
            for contato in self.contatos:
                print(contato)

    def buscar_contato(self, nome):
        encontrados = [c for c in self.contatos if c.nome.lower() == nome.lower()]
        if encontrados:
            for contato in encontrados:
                print(contato)
        else:
            print("Contato não encontrado.")

    def remover_contato(self, nome):
        original = len(self.contatos)
        self.contatos = [c for c in self.contatos if c.nome.lower() != nome.lower()]
        if len(self.contatos) < original:
            print("Contato removido com sucesso.")
        else:
            print("Contato não encontrado.")

def menu(): 
    agenda = Agenda() 
    print("\n--- Agenda de Contatos ---")
    while True: 
        print("\n1. Adicionar Contato") 
        print("2. Listar Contatos") 
        print("3. Buscar Contato") 
        print("4. Remover Contato") 
        print("5. Sair") 
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            agenda.adicionar_contato(nome, telefone)

        elif opcao == "2":
            agenda.listar_contatos()

        elif opcao == "3":
            nome = input("Nome para buscar: ")
            agenda.buscar_contato(nome)

        elif opcao == "4":
            nome = input("Nome para remover: ")
            agenda.remover_contato(nome)

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()