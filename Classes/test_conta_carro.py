import unittest
from conta_carro import ContaCarro

class TestContaCarro(unittest.TestCase):
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

        self.assertEqual(conta_carro.placa, placa)
        self.assertEqual(conta_carro.modelo, modelo)
        self.assertEqual(conta_carro.marca, marca)
        self.assertEqual(conta_carro.ano, ano)
        self.assertEqual(conta_carro.cor, cor)
        self.assertEqual(conta_carro.chassi, chassi)
        self.assertEqual(conta_carro.quilometragem, quilometragem)
        self.assertEqual(conta_carro.preco, preco)
        self.assertEqual(conta_carro.categoria, categoria)

if __name__ == '__main__':
    unittest.main()