# Importando bibliotecas necessárias
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import tkinter as tk
from tkinter import messagebox
import requests

# Configurações do Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

# Configurações do SQLite
db = SQLAlchemy(app)

# Modelo de dados
class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    idade = db.Column(db.Integer, nullable=False)

# Rotas da API
@app.route('/pessoas', methods=['GET'])
def obter_pessoas():
    pessoas = Pessoa.query.all()
    pessoas_json = [{"id": pessoa.id, "nome": pessoa.nome, "email": pessoa.email, "idade": pessoa.idade} for pessoa in pessoas]
    return jsonify({"pessoas": pessoas_json})

@app.route('/pessoas', methods=['POST'])
def cadastrar_pessoa():
    dados = request.json
    nova_pessoa = Pessoa(nome=dados['nome'], email=dados['email'], idade=dados['idade'])
    db.session.add(nova_pessoa)
    db.session.commit()
    return jsonify({"mensagem": "Pessoa cadastrada com sucesso!"})

@app.route('/pessoas/<int:pessoa_id>', methods=['DELETE'])
def excluir_pessoa(pessoa_id):
    pessoa = Pessoa.query.get(pessoa_id)
    if pessoa:
        db.session.delete(pessoa)
        db.session.commit()
        return jsonify({"mensagem": f"Pessoa com ID {pessoa_id} excluída com sucesso!"})
    else:
        return jsonify({"erro": f"Pessoa com ID {pessoa_id} não encontrada"}), 404

# Função para obter pessoas
def obter_pessoas_interface():
    resposta = requests.get('http://localhost:5000/pessoas')
    if resposta.status_code == 200:
        pessoas = resposta.json()['pessoas']
        for pessoa in pessoas:
            print(f"ID: {pessoa['id']}, Nome: {pessoa['nome']}, Email: {pessoa['email']}, Idade: {pessoa['idade']}")
    else:
        print("Erro ao obter pessoas.")

# Interface gráfica usando Tkinter
def cadastrar():
    nome = entry_nome.get()
    email = entry_email.get()
    idade = entry_idade.get()

    # Validando os dados
    if not nome or not email or not idade:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return

    # Enviando os dados para a API
    dados = {"nome": nome, "email": email, "idade": int(idade)}
    resposta = requests.post('http://localhost:5000/pessoas', json=dados)

    if resposta.status_code == 200:
        messagebox.showinfo("Sucesso", "Pessoa cadastrada com sucesso!")
    else:
        messagebox.showerror("Erro", "Erro ao cadastrar pessoa.")

# Função para excluir pessoa pelo ID
def excluir():
    pessoa_id = entry_excluir_id.get()
    if not pessoa_id:
        messagebox.showerror("Erro", "Por favor, informe o ID da pessoa a ser excluída.")
        return

    # Enviando a solicitação para a API
    resposta = requests.delete(f'http://localhost:5000/pessoas/{pessoa_id}')

    if resposta.status_code == 200:
        messagebox.showinfo("Sucesso", f"Pessoa com ID {pessoa_id} excluída com sucesso!")
    elif resposta.status_code == 404:
        messagebox.showerror("Erro", f"Pessoa com ID {pessoa_id} não encontrada.")
    else:
        messagebox.showerror("Erro", f"Erro ao excluir pessoa com ID {pessoa_id}.")

# Criando a interface gráfica
root = tk.Tk()
root.title("Cadastro de Pessoas")

# Campos de entrada para cadastro
tk.Label(root, text="Nome:").grid(row=0, column=0)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1)

tk.Label(root, text="Email:").grid(row=1, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1)

tk.Label(root, text="Idade:").grid(row=2, column=0)
entry_idade = tk.Entry(root)
entry_idade.grid(row=2, column=1)

# Botão de cadastro
btn_cadastrar = tk.Button(root, text="Cadastrar", command=cadastrar)
btn_cadastrar.grid(row=3, column=0, columnspan=2)

# Botão obter pessoas
btn_obter_pessoas = tk.Button(root, text="Obter Pessoas", command=obter_pessoas_interface)
btn_obter_pessoas.grid(row=4, column=0, columnspan=2)

# Campos de entrada para exclusão
tk.Label(root, text="ID para excluir:").grid(row=5, column=0)
entry_excluir_id = tk.Entry(root)
entry_excluir_id.grid(row=5, column=1)

# Botão de exclusão
btn_excluir = tk.Button(root, text="Excluir", command=excluir)
btn_excluir.grid(row=6, column=0, columnspan=2)

# Iniciando a interface gráfica
root.mainloop()
