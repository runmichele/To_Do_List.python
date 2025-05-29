## 📖 Descrição do Projeto
Este é um projeto de **To-Do List** desenvolvido como atividade acadêmica na disciplina de Programação.  
O objetivo é praticar conceitos de estruturas de dados, controle de fluxo e persistência de informações em Python.

## 🚀 Tecnologias e Ferramentas
- **Python  3.12.1**  
- **JSON** para persistência automática das tarefas em `tasks.json`  
- **venv** para criar um ambiente virtual isolado  
- Git & GitHub para versionamento de código 

## 📋 Pré-requisitos
- Python 3.12.1
- (Opcional) Ambiente virtual: `.venv`

## 🛠️ Instalação e execução

```bash
git clone https://github.com/runmichele/To_Do_List.python.git
cd To_Do_List.python

# Cria e ativa venv (opcional)
python -m venv .venv
source .venv/Scripts/activate   # Windows
# source .venv/bin/activate     # macOS/Linux

# Instala dependências (opcional)
pip install -r requirements.txt

# Roda o programa
python to_do_list.py

to_do_list/
├── .venv/            # ambiente virtual (ignorado no Git)
├── tasks.json        # persistência de dados
├── to_do_list.py     # script principal
├── requirements.txt  # dependências (se houver)
└── README.md         # documentação

## ▶️ Exemplo de uso

```text
== MENU ==
1. Adicionar tarefa
2. Listar tarefas
3. Marcar como feita
4. Remover tarefa
0. Sair
Escolha uma opção: 1
Descrição da tarefa:
Comprar leite


