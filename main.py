# main.py

def exibir_menu():
    print("\n--- TO-DO LIST ---")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")

def adicionar_tarefa(tarefas):
    tarefa = input("Digite a tarefa: ")
    tarefas.append({"tarefa": tarefa, "concluida": False})
    print(f"Tarefa '{tarefa}' adicionada!")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        for i, t in enumerate(tarefas, start=1):
            status = "[X]" if t["concluida"] else "[ ]"
            print(f"{i}. {status} {t['tarefa']}")

def marcar_concluida(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa concluída: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True
            print(f"Tarefa '{tarefas[indice]['tarefa']}' marcada como concluída!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa a remover: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefa_removida = tarefas.pop(indice)
            print(f"Tarefa '{tarefa_removida['tarefa']}' removida!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

def main():
    tarefas = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            marcar_concluida(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "5":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
