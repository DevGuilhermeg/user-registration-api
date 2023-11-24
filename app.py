import psycopg2
from psycopg2 import sql

# Substitua essas informações com as suas
host = "dpg-clgivcug1b2c73a92k5g-a"
port = 5432
user = "usuarios_n9tr_user"
password = "X3M5m7QVIRRVGvdgFaPNIUjZTp5f4yDi"
database = "postgres://usuarios_n9tr_user:X3M5m7QVIRRVGvdgFaPNIUjZTp5f4yDi@dpg-clgivcug1b2c73a92k5g-a/usuarios_n9tr"

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
