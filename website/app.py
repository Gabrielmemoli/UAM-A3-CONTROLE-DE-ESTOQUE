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
        cursor.execute("INSERT INTO veiculos (placa, modelo, chassi, ano, cor, km, preco, marca, categoria, status, imagem) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (placa, modelo, chassi, ano, cor, km, preco, marca, categoria, status, imagem))
        conn.commit()
        conn.close()

        # Redirecionar para uma página de sucesso ou exibir uma mensagem
        return 'Veículo cadastrado com sucesso!'

    # Lógica para exibir o formulário de cadastro de veículo
    return render_template('cadastro_carros.html')

@app.route('/listCars')
def listCars():
    # Conectar ao banco de dados
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()

    # Recuperar os carros do banco de dados
    cursor.execute('SELECT placa, modelo, cor, km, preco, marca, categoria, status, imagem FROM veiculos')
    carros = cursor.fetchall()

    # Fechar a conexão com o banco de dados
    conn.close()

    # Renderizar o template HTML e passar os dados dos carros
    return render_template('listCars.html', carros=carros)

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

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
