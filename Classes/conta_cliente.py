import sys
import os
import sqlite3
import unittest

# Get the absolute path of the directory containing the module
module_dir = os.path.dirname(os.path.abspath(__file__))
conta_cliente_dir = os.path.join(module_dir, 'path/to/conta_cliente')  # Replace 'path/to/conta_carro' with the actual directory path

# Add the module directory to the sys.path list
sys.path.append(conta_cliente_dir)

import conta_cliente

class AccountTests(unittest.TestCase):
    def setUp(self):
        # Connect to an in-memory SQLite database
        self.connection = sqlite3.connect(":memory:")
        self.cursor = self.connection.cursor()

        # Create a table for accounts
        self.cursor.execute("""
            CREATE TABLE accounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT,
                password TEXT,
                cpf TEXT,
                login TEXT
            )
        """)

    def tearDown(self):
        # Drop the accounts table and close the database connection
        self.cursor.execute("DROP TABLE accounts")
        self.connection.close()

    def test_account_creation(self):
        name = "Gabriel Memoli"
        email = "gabriel@anhembi.com"
        password = "senha123"
        cpf = "123456789"
        login = "gabriel"

        account = conta_cliente.Account(name, email, password, cpf, login)

        # Insert the account into the database
        self.cursor.execute("""
            INSERT INTO accounts (name, email, password, cpf, login)
            VALUES (?, ?, ?, ?, ?)
        """, (name, email, password, cpf, login))
        self.connection.commit()

        # Retrieve the account from the database
        self.cursor.execute("SELECT * FROM accounts WHERE id = ?", (account.id,))
        result = self.cursor.fetchone()

        # Assert that the retrieved account matches the expected values
        self.assertEqual(result[1], name)
        self.assertEqual(result[2], email)
        self.assertEqual(result[3], password)
        self.assertEqual(result[4], cpf)
        self.assertEqual(result[5], login)

if __name__ == '__main__':
    unittest.main()