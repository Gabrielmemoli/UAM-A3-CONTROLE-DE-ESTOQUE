import unittest
from conta_cliente import Account

class AccountPageTests(unittest.TestCase):
    def test_account_creation(self):
        name = "Gabriel Memoli"
        email = "gabriel@anhembi.com"
        password = "senha123"
        cpf = "123456789"
        login = "gabriel"

        account = Account(name, email, password, cpf, login)

        self.assertEqual(account.name, name)
        self.assertEqual(account.email, email)
        self.assertEqual(account.password, password)
        self.assertEqual(account.cpf, cpf)
        self.assertEqual(account.login, login)

if __name__ == '__main__':
    unittest.main()