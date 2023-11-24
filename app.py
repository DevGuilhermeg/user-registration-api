from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://usuarios_n9tr_user:X3M5m7QVIRRVGvdgFaPNIUjZTp5f4yDi@12.12.0.0/0/usuarios_n9tr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

db = SQLAlchemy(app)



class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    senha = db.Column(db.String(60), nullable=False)

# Cria as tabelas no banco de dados
with app.app_context():
    db.create_all()

@app.route('/teste-conexao-bd', methods=['GET'])
def teste_conexao_bd():
    try:
        # Adiciona uma pessoa ao banco de dados
        nova_pessoa = Pessoa(nome="Exemplo", email="exemplo@email.com", idade=25)
        db.session.add(nova_pessoa)
        db.session.commit()

        return jsonify({"mensagem": "Conexão com o banco de dados bem-sucedida e registro adicionado."})
    except Exception as e:
        return jsonify({"erro": f"Erro na conexão com o banco de dados: {str(e)}"}), 500

if __name__ == '__main__':
    # Inicia o servidor Flask em modo de depuração
    app.run(debug=True)
