import sys
import os

# Get the absolute path of the directory containing the module
module_dir = os.path.dirname(os.path.abspath(__file__))
conta_carro_dir = os.path.join(module_dir, 'path/to/conta_carro')  # Replace 'path/to/conta_carro' with the actual directory path

# Add the module directory to the sys.path list
sys.path.append(conta_carro_dir)

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