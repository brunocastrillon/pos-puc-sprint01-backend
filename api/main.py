from flask import redirect
from flask_cors import CORS
from flask_openapi3 import OpenAPI
from flask_jwt_extended import JWTManager
from flasgger import Swagger

from config.settings import Config
from config.swagger_config import swagger_config

from db.database import db

from routes.autenticar_routes import autenticar_bp
from routes.comentario_routes import comentario_bp
from routes.curtida_routes import curtida_bp
from routes.postagem_routes import postagem_bp

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

# Registrando rotas
app.register_blueprint(autenticar_bp, url_prefix="/api")
app.register_blueprint(comentario_bp, url_prefix="/api")
app.register_blueprint(curtida_bp, url_prefix="/api")
app.register_blueprint(postagem_bp, url_prefix="/api")

@app.route("/")
def home():
    return redirect("/apidocs")

if __name__ == "__main__":
    app.run(debug=True)