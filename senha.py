import sqlite3

master_senha = "02100402001"

senha = input("Insira sua senha master: ")
if senha != master_senha:
    print("Senha inválida! Encerrando...")
    exit()

conn = sqlite3.connect('senha.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    senha TEXT NOT NULL
);
''')

def menu():
    print("*******************************")
    print("* i : inserir nova senha      *")
    print("* l : listar serviços salvos  *")
    print("* r : recuperar uma senha     *")
    print("* s : sair                    *")
    print("*******************************")

def get_senha(service):
    cursor.execute(f'''
        SELECT (username, senha) From users
        WHERE service = '{service}'
    ''')

    if cursor.rowcount ==0:
        print("Serviço não cadastrado (use 'l' para verificar os serviços).")
    else:
        for user in cursor.fetchall():
            print(user)

def insert_senha(cursor, service, username, senha):
    cursor.execute(f'''
        INSERT INTO users (service, username, senha) 
        VALUES ('{service}', '{username}', '{senha}')
    ''') 
    conn.commit()


def show_services():
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)

while True:
    menu()
    op = input("o que deseja fazer? ")
    if op not in ['l', 'i', 'r', 's']:
        print("opção invalida!")
        continue

    if op == 's':
        break

    if op == 'i':
        service = input('Qual o nome do serviço? ')
        username = input('Qual o nome de usuario? ')
        senha = input('Qual a senha? ')
        insert_senha(service, username, senha)

    if op == 'l': 
        show_services()

    if op =='r':
        service = input('Qual o serviço para o qual quer a senha? ')
        get_senha(service)
conn.close()