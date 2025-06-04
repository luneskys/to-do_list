# Cria uma lista vazia para armazenar as tarefas
tarefas = []

# Função para adicionar uma nova tarefa à lista
def add_tarefa():
    # Solicita ao usuário que digite uma tarefa
    tarefa = input("Digite a tarefa: ").strip()
    # Verifica se a tarefa não está vazia
    if tarefa:
        # Adiciona a tarefa à lista
        tarefas.append(tarefa)
        # Exibe mensagem de confirmação
        print(f'Tarefa "{tarefa}" adicionada!')
    else:
        # Caso o usuário tenha digitado algo vazio
        print("⚠️ Tarefa vazia não adicionada.")

# Função para listar todas as tarefas cadastradas
def list_tarefa():
    # Verifica se a lista está vazia
    if not tarefas:
        # Informa que não há tarefas
        print("📭 Nenhuma tarefa.")
    else:
        # Exibe todas as tarefas com numeração
        print("📋 Tarefas:")
        for i, tarefa in enumerate(tarefas, 1):  # começa a contagem em 1
            print(f"{i}. {tarefa}")

# Função para remover uma tarefa específica pelo número
def remove_tarefa():
    # Lista as tarefas atuais
    list_tarefa()
    # Se a lista estiver vazia, encerra a função
    if not tarefas:
        return
    try:
        # Solicita ao usuário o número da tarefa a ser removida
        num = int(input("Número da tarefa para remover: "))
        # Verifica se o número está dentro do intervalo válido
        if 1 <= num <= len(tarefas):
            # Remove a tarefa e guarda o nome
            removed = tarefas.pop(num - 1)
            # Exibe mensagem de confirmação
            print(f'🗑️ Tarefa "{removed}" removida!')
        else:
            # Caso o número não exista na lista
            print("❌ Número inválido.")
    except ValueError:
        # Caso o usuário não digite um número
        print("⚠️ Entrada inválida. Digite um número.")

# Função principal que controla o menu do programa
def main():
    # Loop infinito até o usuário escolher sair
    while True:
        # Exibe o menu de opções
        print("\n--- MENU TO-DO ---")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Remover Tarefa")
        print("4. Sair")
        # Lê a escolha do usuário
        choice = input("Escolha: ").strip()

        # Verifica a opção escolhida e chama a função correspondente
        if choice == '1':
            add_tarefa()
        elif choice == '2':
            list_tarefa()
        elif choice == '3':
            remove_tarefa()
        elif choice == '4':
            # Sai do programa
            print("👋 Saindo. Até mais!")
            break
        else:
            # Caso o usuário escolha uma opção inválida
            print("❌ Opção inválida.")

# Ponto de entrada do programa (executa o menu se o arquivo for executado diretamente)
if __name__ == "__main__":
    main()

