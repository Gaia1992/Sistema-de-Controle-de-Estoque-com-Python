import os



# Dicionário para armazenar os produtos
estoque = {}

def limpar():
    os.system('cls')

# Função para adicionar produto
def adicionar_produto():
    
    nome = input(f"NOME DO PRODUTO: ")
    if nome in estoque:
        print("Produto já existe no estoque!")
    else:
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade em estoque: "))
        estoque[nome] = {'preco': preco, 'quantidade': quantidade}
        print(f"Produto '{nome}' adicionado com sucesso!")

# Função para atualizar produto
def atualizar_produto():
   
    nome = input("Digite o nome do produto para atualizar: ")
    if nome in estoque:
        preco = float(input("Digite o novo preço do produto: "))
        quantidade = int(input("Digite a nova quantidade em estoque: "))
        estoque[nome] = {'preco': preco, 'quantidade': quantidade}
        print(f"Produto '{nome}' atualizado com sucesso!")
    else:
        print("Produto não encontrado!")

# Função para excluir produto
def excluir_produto():
    
    nome = input("Digite o nome do produto para excluir: ")
    if nome in estoque:
        del estoque[nome]
        print(f"Produto '{nome}' excluído com sucesso!")
    else:
        print("Produto não encontrado!")

# Função para visualizar estoque
def visualizar_estoque():
    
    if estoque:
        print("Estoque atual:")
        for nome, detalhes in estoque.items():
            print(f"Nome: {nome}, Preço: R${detalhes['preco']}, Quantidade: {detalhes['quantidade']}")
    else:
        print("O estoque está vazio!")

# Função principal para exibir o menu
def menu():
    while True:
        
        print("\nMenu de Opções:")
        print("1. Adicionar Produto")
        print("2. Atualizar Produto")
        print("3. Excluir Produto")
        print("4. Visualizar Estoque")
        print("5. Sair")
        
        escolha = input("Escolha uma opção (1-5): ")
        
        if escolha == '1':
            adicionar_produto()
        elif escolha == '2':
            atualizar_produto()
        elif escolha == '3':
            excluir_produto()
        elif escolha == '4':
            visualizar_estoque()
        elif escolha == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Iniciar o sistema
menu()