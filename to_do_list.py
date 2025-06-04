# Lista para armazenar as tarefas
tarefas = []

# Função para adicionar uma nova tarefa
def add_tarefa():
    tarefa = input("Digite a tarefa: ").strip()
    if tarefa:
        tarefas.append(tarefa)
        print(f'Tarefa "{tarefa}" adicionada!')
    else:
        print("⚠️ Tarefa vazia não adicionada.")

# Função para listar todas as tarefas
def list_tarefa():
    if not tarefas:
        print("📭 Nenhuma tarefa.")
    else:
        print("📋 Tarefas:")
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")

# Função para remover uma tarefa pelo número
def remove_tarefa():
    list_tarefa()
    if not tarefas:
        return
    try:
        num = int(input("Número da tarefa para remover: "))
        if 1 <= num <= len(tarefas):
            removed = tarefas.pop(num - 1)
            print(f'🗑️ Tarefa "{removed}" removida!')
        else:
            print("❌ Número inválido.")
    except ValueError:
        print("⚠️ Entrada inválida. Digite um número.")

# Menu principal
def main():
    while True:
        print("\n--- MENU TO-DO ---")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Remover Tarefa")
        print("4. Sair")
        choice = input("Escolha: ").strip()

        if choice == '1':
            add_tarefa()
        elif choice == '2':
            list_tarefa()
        elif choice == '3':
            remove_tarefa()
        elif choice == '4':
            print("👋 Saindo. Até mais!")
            break
        else:
            print("❌ Opção inválida.")

# Executa o programa
if __name__ == "__main__":
    main()

