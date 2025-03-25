from flask_cors import CORS
from flask_openapi3 import OpenAPI
from flasgger import Swagger
from flask_jwt_extended import JWTManager
from config.settings import Config
from config.swagger_config import swagger_config
from db.database import db

app = OpenAPI(__name__)
app.config.from_object(Config)

# Permite requisições do frontend
CORS(app)               

# Inicializar o banco de dados
db.init_app(app)

# Criando o banco ao iniciar
with app.app_context():
    db.create_all()

# Inicializando o Gerenciador de Tokens para autenticação/autorização
jwt = JWTManager(app) 

# Configuração do Swagger com suporte a JWT
swagger = Swagger(app, config=swagger_config)

if __name__ == "__main__":
    app.run(debug=True)