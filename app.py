from flask import Flask, render_template, request, redirect
import requests
from tkinter import messagebox

app = Flask(__name__)


url_pessoas = 'https://api-usuarios-tvdy.onrender.com/pessoas'
# URL da API para login
url_login = 'https://api-usuarios-tvdy.onrender.com/login'
url_cadastrar = 'https://api-usuarios-tvdy.onrender.com/pessoas'


@app.route('/')
def index():
    # Obtenha o email do parâmetro na URL
    email = request.args.get('email')
    dados_usuario = None
    nome = "Recrutador"
    
    # Se o email estiver presente, faça a solicitação à API para obter dados do usuário, se necessário
    if email:
        urlEmail = f'https://api-usuarios-tvdy.onrender.com/pessoas/email/{email}'
        resposta = requests.get(urlEmail)

        if resposta.status_code == 200:
            # Aqui você pode usar os dados do usuário obtidos da API
            dados_usuario = resposta.json()
            nome = (dados_usuario['pessoa']['nome'])

            # ...
    
    # Restante do código da rota /index
    
    saldaçao = f"Olá, {nome}! Guilherme aqui"
    print(saldaçao)
    
    return render_template('index.html', nome=saldaçao)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/fazer-login', methods=['POST'])
def fazer_login():
    # Obter os valores do formulário
    email = request.form.get('email')
    senha = request.form.get('senha')

    # Dados de login em formato JSON
    dados_login = {'email': email, 'senha': senha}

    # Fazendo a requisição POST para o endpoint de login com os dados em JSON
    resposta = requests.post(url_login, json=dados_login, verify=True)  # O parâmetro 'verify=True' verifica o certificado SSL

    # Verificando o status da resposta
    if resposta.status_code == 200:
        # Redirecionar para a página principal ou outra página após o login bem-sucedido
        return redirect(f'/?email={email}')
    else:
        return f"Falha no login. Código de status: {resposta.status_code}"
    

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    # Obter os valores do formulário
    nome = request.form.get('nameC')
    email = request.form.get('emailC')
    idade = request.form.get("idadeC")
    senha = request.form.get('senhaC')

    dados = {"nome": nome, "email": email, "idade": int(idade), "senha": senha}
    resposta = requests.post(url_cadastrar, json=dados)

    if resposta.status_code == 200:
        mensagem = "Pessoa cadastrada com sucesso!"
        # Retornar a mensagem de sucesso para ser renderizada na página HTML
        return render_template('cadastro.html', mensagem=mensagem)
    else:
        mensagem = "Erro ao cadastrar pessoa."
        # Retornar a mensagem de erro para ser renderizada na página HTML
        return render_template('cadastro.html', mensagem_erro=mensagem)
if __name__ == '__main__':
    app.run(debug=True)
