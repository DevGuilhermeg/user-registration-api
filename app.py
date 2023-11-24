from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://cadastro_usuario_user:ZEeEUZKLOE21ZUprGPLy1rWlmD0S9DLx@dpg-cleo2lbl00ks739s9660-a/cadastro_usuario'
db = SQLAlchemy(app)

@app.route('/teste-conexao-bd', methods=['GET'])
def teste_conexao_bd():
    try:
        result = db.engine.execute(text("SELECT 1"))
        if result.scalar() == 1:
            return jsonify({"mensagem": "Conexão com o banco de dados bem-sucedida."})
        else:
            return jsonify({"erro": "A consulta não retornou o valor esperado."}), 500
    except Exception as e:
        return jsonify({"erro": f"Erro na conexão com o banco de dados: {str(e)}"}), 500

