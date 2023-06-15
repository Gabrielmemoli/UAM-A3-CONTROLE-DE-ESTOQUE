from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
app.secret_key = 'mysecretkey'

# Função para criar a tabela 'users' no banco de dados
def create_table():
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS veiculos (
        placa TEXT,
        modelo TEXT,
        chassi TEXT,
        ano INTEGER,
        cor TEXT,
        km INTEGER,
        preco REAL,
        marca TEXT,
        categoria TEXT,
        status TEXT,
        imagem BLOB
    )
    ''')

    # Criar tabela usuarios
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT,
        password TEXT
    )
    ''')

    conn.commit()
    conn.close()

    # Página inicial com formulário de login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            return redirect('/portfolio')  # Redireciona para a página "portfolio.html"
        else:
            return render_template('login.html', error=True)
    return render_template('login.html', error=False)

# Página de cadastro de usuário
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Obter os dados do formulário
        username = request.form['username']
        password = request.form['password']

        # Salvar os dados no banco de dados
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('register.html')



# Página "portfolio" após o login
@app.route('/portfolio')
def exibir_portfolio():
    return render_template('portfolio.html')

# Rota para a página de cadastro de carros
#@app.route('/cadastro_carros')
#def cadastro_carros():
#    return render_template('cadastro_carros.html')

@app.route('/portfolio/<placa>', methods=['POST'])
def excluir_carro(placa):
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()

    # Executa a query SQL para excluir o carro com a placa fornecida
    cursor.execute('DELETE FROM veiculos WHERE placa = ?', (placa,))
    conn.commit()

    # Fecha a conexão com o banco de dados
    conn.close()

    # Redirecionar para a página principal após a exclusão
    return redirect('/portfolio')

@app.route('/edit_carro/<placa>', methods=['GET', 'POST'])
def edit_carro(placa):
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        # Obter os novos valores dos campos do formulário de edição
        modelo = request.form['modelo']
        cor = request.form['cor']
        km = request.form['km']
        preco = request.form['preco']
        marca = request.form['marca']
        categoria = request.form['categoria']
        status = request.form['status']

        # Executar a query SQL para atualizar as informações do veículo
        cursor.execute("UPDATE veiculos SET modelo = ?, cor = ?, km = ?, preco = ?, marca = ?, categoria = ?, status = ? WHERE placa = ?",
                       (modelo, cor, km, preco, marca, categoria, status, placa))
        conn.commit()

        # Redirecionar para a página de portfólio após a edição
        return redirect('/portfolio')

    else:
        # Obter as informações do veículo com base na placa fornecida
        cursor.execute('SELECT * FROM veiculos WHERE placa = ?', (placa,))
        veiculo = cursor.fetchone()

        # Renderizar a página de edição de carro com as informações do veículo
        return render_template('edit_carro.html', veiculo=veiculo)


@app.route('/cadastro_carros', methods=['GET', 'POST'])
def cadastro_carros():
    if request.method == 'POST':
        # Obter os dados do formulário
        placa = request.form['placa']
        modelo = request.form['modelo']
        chassi = request.form['chassi']
        ano = request.form['ano']
        cor = request.form['cor']
        km = request.form['km']
        preco = request.form['preco']
        marca = request.form['marca']
        categoria = request.form['categoria']
        status = request.form['status']
        imagem = request.form['imagem']

        # Salvar os dados no banco de dados
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO veiculos VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                       (placa, modelo, chassi, ano, cor, km, preco, marca, categoria, status, imagem))
        conn.commit()
        conn.close()

        # Redirecionar para a página de portfólio após o cadastro
        return redirect('/portfolio')

    else:
        return render_template('cadastro_carros.html')


@app.route('/portfolio')
def portfolio():
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()

    # Selecionar todos os veículos do banco de dados
    cursor.execute('SELECT * FROM veiculos')
    veiculos = cursor.fetchall()

    # Renderizar a página de portfólio com a lista de veículos
    return render_template('portfolio.html', veiculos=veiculos)

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
