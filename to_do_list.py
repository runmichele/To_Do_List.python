import json
import os

tasks = []

def add_task():
    desc = input("Descrição da tarefa:\n")
    tasks.append({'desc': desc, 'done': False})

def list_tasks():
    for i, t in enumerate(tasks):
        status = "✓" if t['done'] else "✗"
        print(f"{i}. [{status}] {t['desc']}")

def mark_done():
    idx = int(input("Índice da tarefa concluída:\n"))
    tasks[idx]['done'] = True

def remove_task():
    idx = int(input("Índice da tarefa para remover:\n"))
    tasks.pop(idx)

while True:
    print("\n== MENU ==")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como feita")
    print("4. Remover tarefa")
    print("0. Sair")
    opc = input("Escolha uma opção: ")

    if opc == "1":
        add_task()
    elif opc == "2":
        list_tasks()
    elif opc == "3":
        mark_done()
    elif opc == "4":
        remove_task()
    elif opc == "0":
        break
    else:
        print("Opção inválida.")
