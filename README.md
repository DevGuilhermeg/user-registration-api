# README: API de Cadastro de Pessoas

Este é um simples exemplo de uma API de cadastro de pessoas usando Flask e SQLAlchemy. A API permite operações básicas de CRUD (Create, Read, Update, Delete) para gerenciar informações de pessoas em um banco de dados PostgreSQL.

## Configuração do Ambiente

Antes de executar a aplicação, certifique-se de ter as dependências instaladas. Recomenda-se o uso de um ambiente virtual para evitar conflitos com outras dependências do sistema. Execute o seguinte comando para instalar as dependências:

```bash
pip install -r requirements.txt
```

## Configuração do Banco de Dados

A aplicação utiliza um banco de dados PostgreSQL. Certifique-se de configurar corretamente a URI do banco de dados no arquivo `app.py`. Você pode ajustar a configuração no trecho:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://seu_usuario:sua_senha@seu_host/seu_banco_de_dados'
```

Substitua `'seu_usuario'`, `'sua_senha'`, `'seu_host'`, e `'seu_banco_de_dados'` pelos detalhes de conexão do seu banco de dados PostgreSQL.

## Executando a Aplicação

Para iniciar a aplicação, execute o seguinte comando:

```bash
python app.py
```

A aplicação será executada localmente em `http://127.0.0.1:5000/`.

## Rotas Disponíveis

### `GET /pessoas`

Obtém uma lista de todas as pessoas cadastradas.

### `POST /pessoas`

Cadastra uma nova pessoa. Enviar dados no formato JSON no corpo da requisição, incluindo "nome", "email", "idade" e "senha".

### `DELETE /pessoas/<int:pessoa_id>`

Exclui a pessoa com o ID especificado.

### `GET /pessoas/email/<string:email>`

Obtém informações sobre a pessoa com o email especificado.

### `POST /login`

Realiza o login. Enviar dados no formato JSON no corpo da requisição, incluindo "email" e "senha".

## Erros Comuns

- **400 Bad Request:** Campos obrigatórios ausentes ou formato inválido.
- **401 Unauthorized:** Credenciais inválidas durante o login.
- **404 Not Found:** Pessoa não encontrada com o ID ou email especificado.

Lembre-se de ajustar as configurações conforme necessário para o seu ambiente de desenvolvimento e banco de dados. Este é um exemplo básico e pode ser expandido conforme as necessidades do seu projeto.
