from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://cadastro_usuario_user:ZEeEUZKLOE21ZUprGPLy1rWlmD0S9DLx@dpg-cleo2lbl00ks739s9660-a/cadastro_usuario'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

db = SQLAlchemy(app)

@app.route('/teste-conexao-bd', methods=['GET'])
def teste_conexao_bd():
    try:
        db.session.query("1").from_statement("SELECT 1").all()
        return jsonify({"mensagem": "Conexão com o banco de dados bem-sucedida."})
    except Exception as e:
        return jsonify({"erro": f"Erro na conexão com o banco de dados: {str(e)}"}), 500

