import psycopg2
from psycopg2 import sql

# Substitua essas informações com as suas
host = "dpg-clgjee58td7s73bi9dkg-a"
port = 5432
user = "bando_usuarios_29xx_user"
password = "ZaB44taTeXiTopMZsBlU8kmjultHhEqJ"
database = "bando_usuarios_29xx"

# Conectar ao servidor PostgreSQL
conn = psycopg2.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database="postgres"  # Conecte-se ao banco de dados "postgres" para criar um novo banco de dados
)

# Criar um cursor
cursor = conn.cursor()

# Criar um novo banco de dados
cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(database)))

# Conceder permissões ao usuário sobre o novo banco de dados
cursor.execute(sql.SQL("GRANT ALL PRIVILEGES ON DATABASE {} TO {}").format(
    sql.Identifier(database),
    sql.Identifier(user)
))

# Fechar a conexão
conn.close()
