import sys
import os

# Get the absolute path of the directory containing the module
module_dir = os.path.dirname(os.path.abspath(__file__))
conta_cliente_dir = os.path.join(module_dir, 'path/to/conta_cliente')  # Replace 'path/to/conta_carro' with the actual directory path

# Add the module directory to the sys.path list
sys.path.append(conta_cliente_dir)

class Account:
    def __init__(self, name, email, password, cpf, login):
        self.name = name
        self.email = email
        self.password = password
        self.cpf = cpf
        self.login = login