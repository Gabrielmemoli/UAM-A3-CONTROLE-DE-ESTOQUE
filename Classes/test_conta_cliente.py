import unittest
import sqlite3

class Account:
    def __init__(self, name, email, password, cpf, login):
        self.name = name
        self.email = email
        self.password = password
        self.cpf = cpf
        self.login = login
        self.id = None

    def save(self):
        # Conecta ao banco de dados
        connection = sqlite3.connect("banco.db")
        cursor = connection.cursor()

        # Insere a conta no banco de dados
        cursor.execute("""
            INSERT INTO accounts (name, email, password, cpf, login)
            VALUES (?, ?, ?, ?, ?)
        """, (self.name, self.email, self.password, self.cpf, self.login))
        self.id = cursor.lastrowid

        # Fecha a conexão com o banco de dados
        connection.commit()
        connection.close()

class AccountPageTests(unittest.TestCase):
    def setUp(self):
        # Cria a tabela accounts no banco de dados
        self.connection = sqlite3.connect("banco.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT,
                password TEXT,
                cpf TEXT,
                login TEXT
            )
        """)

    def tearDown(self):
        # Apaga a tabela accounts do banco de dados
        self.cursor.execute("DROP TABLE IF EXISTS accounts")
        self.connection.commit()
        self.connection.close()

    def test_account_creation(self):
        name = "Gabriel Memoli"
        email = "gabriel@anhembi.com"
        password = "senha123"
        cpf = "123456789"
        login = "gabriel"

        account = Account(name, email, password, cpf, login)
        account.save()

        # Recupera a conta do banco de dados
        self.cursor.execute("SELECT * FROM accounts WHERE id = ?", (account.id,))
        result = self.cursor.fetchone()

        # Verifica se os dados da conta estão corretos
        self.assertEqual(result[1], name)
        self.assertEqual(result[2], email)
        self.assertEqual(result[3], password)
        self.assertEqual(result[4], cpf)
        self.assertEqual(result[5], login)

if __name__ == '__main__':
    unittest.main()