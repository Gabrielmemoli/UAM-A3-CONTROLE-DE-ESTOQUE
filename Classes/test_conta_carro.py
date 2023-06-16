import unittest
import sqlite3

class ContaCarro:
    def __init__(self, placa, modelo, marca, ano, cor, chassi, quilometragem, preco, categoria):
        self.placa = placa
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.cor = cor
        self.chassi = chassi
        self.quilometragem = quilometragem
        self.preco = preco
        self.categoria = categoria
        self.id = None

    def save(self):
        # Conecta ao banco de dados
        connection = sqlite3.connect("banco.db")
        cursor = connection.cursor()

        # Insere o carro no banco de dados
        cursor.execute("""
            INSERT INTO carros (placa, modelo, marca, ano, cor, chassi, quilometragem, preco, categoria)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (self.placa, self.modelo, self.marca, self.ano, self.cor, self.chassi, self.quilometragem, self.preco, self.categoria))
        self.id = cursor.lastrowid

        # Fecha a conexão com o banco de dados
        connection.commit()
        connection.close()

class TestContaCarro(unittest.TestCase):
    def setUp(self):
        # Cria a tabela carros no banco de dados
        self.connection = sqlite3.connect("banco.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS carros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                placa TEXT,
                modelo TEXT,
                marca TEXT,
                ano INTEGER,
                cor TEXT,
                chassi TEXT,
                quilometragem INTEGER,
                preco REAL,
                categoria TEXT
            )
        """)

    def tearDown(self):
        # Apaga a tabela carros do banco de dados
        self.cursor.execute("DROP TABLE IF EXISTS carros")
        self.connection.commit()
        self.connection.close()

    def test_criacao_conta_carro(self):
        placa = "GHYH4444"
        modelo = "FD3S"
        marca = "Mazda"
        ano = 2002
        cor = "Rosa"
        chassi = "1234567890"
        quilometragem = 25000
        preco = 50000000.0
        categoria = "Esportivo"

        conta_carro = ContaCarro(placa, modelo, marca, ano, cor, chassi, quilometragem, preco, categoria)
        conta_carro.save()

        # Recupera o carro do banco de dados
        self.cursor.execute("SELECT * FROM carros WHERE id = ?", (conta_carro.id,))
        result = self.cursor.fetchone()

        # Verifica se os dados do carro estão corretos
        self.assertEqual(result[1], placa)
        self.assertEqual(result[2], modelo)
        self.assertEqual(result[3], marca)
        self.assertEqual(result[4], ano)
        self.assertEqual(result[5], cor)
        self.assertEqual(result[6], chassi)
        self.assertEqual(result[7], quilometragem)
        self.assertEqual(result[8], preco)
        self.assertEqual(result[9], categoria)

if __name__ == '__main__':
    unittest.main()