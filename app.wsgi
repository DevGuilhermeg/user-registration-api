import sys
import os

# Adicione o caminho do diretório da aplicação ao PYTHONPATH
sys.path.insert(0, '/app.py')

# Ative o ambiente virtual, se estiver usando um
activate_this = os.path.join('venv\Scripts\activate')
exec(open(activate_this).read(), {'__file__': activate_this})

# Importe a aplicação Flask
from sua_aplicacao import app as application
