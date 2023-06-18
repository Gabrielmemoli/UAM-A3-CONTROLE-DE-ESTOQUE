import unittest
import sqlite3
from flask import Flask
from app import app, create_table, excluir_carro, edit_carro, cadastro_carros, portfolio, login, register, exibir_portfolio
from flask import render_template, request, redirect

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

        # Configurar o banco de dados de teste
        self.conn = sqlite3.connect('test/test.db')
        self.cursor = self.conn.cursor()
        create_table()

    def tearDown(self):
        # Fecha a conexão com o banco de dados
        self.cursor.close()
        self.conn.close()

    def test_excluir_carro(self):
        # Insere um carro de teste no banco de dados
        self.cursor.execute("INSERT INTO veiculos VALUES ('ABC123', 'Celta', '123456', 2022, 'Roxo', 10000, 150, 'Chevrolet', 'Compacto', 'Disponível')")
        self.conn.commit()

        # Envia uma requisição POST para excluir o carro
        response = self.app.post('/portfolio/ABC123')
        self.assertEqual(response.status_code, 302)

        # Checa se o carro foi excluído do banco de dados
        self.cursor.execute("SELECT * FROM veiculos WHERE placa = 'ABC123'")
        result = self.cursor.fetchone()
        self.assertIsNone(result)

    def test_edit_carro(self):
        # Insere um carro de teste no banco de dados
        self.cursor.execute("INSERT INTO veiculos VALUES ('ABC123', 'Celta', '123456', 2022, 'Roxo', 10000, 150.00, 'Chevrolet', 'Compacto', 'Disponível')")
        self.conn.commit()

        # Envia uma requisição POST para editar o carro
        data = {
            'modelo': 'Corsa',
            'chassi': '654321',
            'ano': 2023,
            'cor': 'Vermelho',
            'km': 20000,
            'preco': 200.00,
            'marca': 'Chevrolet',
            'categoria': 'Compacto',
            'status': 'Alugado'
        }
        response = self.app.post('/edit_carro/ABC123', data=data)
        self.assertEqual(response.status_code, 302)

        # Checa se o carro foi editado no banco de dados
        self.cursor.execute("SELECT * FROM veiculos WHERE placa = 'ABC123'")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[1], 'Corsa')
        self.assertEqual(result[2], '654321')
        self.assertEqual(result[3], 2023)
        self.assertEqual(result[4], 'Vermelho')
        self.assertEqual(result[5], 20000)
        self.assertEqual(result[6], 200.00)
        self.assertEqual(result[7], 'Chevrolet')
        self.assertEqual(result[8], 'Compacto')
        self.assertEqual(result[9], 'Alugado')

    def test_cadastro_carros(self):
        # Envia uma requisição POST para cadastrar um novo carro
        data = {
            'placa': 'FBC123',
            'modelo': 'City',
            'chassi': '444456',
            'ano': 2022,
            'cor': 'Preto',
            'km': 10000,
            'preco': 300.00,
            'marca': 'Honda',
            'categoria': 'Sedan',
            'status': 'Disponível'
        }
        response = self.app.post('/cadastro_carros', data=data)
        self.assertEqual(response.status_code, 302)

        # Checa se o carro foi adicionado ao banco de dados
        self.cursor.execute("SELECT * FROM veiculos WHERE placa = 'FBC123'")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[1], 'City')
        self.assertEqual(result[2], '444456')
        self.assertEqual(result[3], 2022)
        self.assertEqual(result[4], 'Preto')
        self.assertEqual(result[5], 10000)
        self.assertEqual(result[6], 300.00)
        self.assertEqual(result[7], 'Honda')
        self.assertEqual(result[8], 'Sedan')
        self.assertEqual(result[9], 'Disponível')


if __name__ == '__main__':
    unittest.main()