from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://cadastro_usuario_user:ZEeEUZKLOE21ZUprGPLy1rWlmD0S9DLx@dpg-cleo2lbl00ks739s9660-a/cadastro_usuario'
db = SQLAlchemy(app)

@app.route('/teste-conexao-bd', methods=['GET'])
def teste_conexao_bd():
    try:
        db.session.execute("SELECT 1").scalar()
        return jsonify({"mensagem": "Conexão com o banco de dados bem-sucedida."})
    except Exception as e:
        return jsonify({"erro": f"Erro na conexão com o banco de dados: {str(e)}"}), 500

