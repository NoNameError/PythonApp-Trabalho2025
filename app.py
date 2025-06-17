from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    termo = request.form['termo']
    conn = get_db_connection()
    usuarios = conn.execute("SELECT * FROM usuarios WHERE nome LIKE ? OR email LIKE ?",
                            ('%' + termo + '%', '%' + termo + '%')).fetchall()
    conn.close()
    return render_template('resultado.html', usuarios=usuarios, termo=termo)

@app.route('/novo')
def novo():
    return render_template('add.html')

@app.route('/add', methods=['POST'])
def add():
    nome = request.form['nome']
    email = request.form['email']
    conn = get_db_connection()
    conn.execute('INSERT INTO usuarios (nome, email) VALUES (?, ?)', (nome, email))
    conn.commit()
    conn.close()
    return f'Usuário {nome} adicionado com sucesso! <br><a href=\"/\">Voltar</a>'

if __name__ == '__main__':
    app.run(debug=True)
