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

    


if __name__ == '__main__':
    unittest.main()