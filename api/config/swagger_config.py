swagger_config = {
    "headers": [],    
    "openapi": "3.0.0",
    "info": {
        "title": "Microblog Minimalista - API",
        "version": "1.0",
        "description": "Documentação da API do Microblog Minimalista",
        "contact": {
            "name": "Suporte API",
            "email": "brunocastrillon@gmail.com"
        }
    },
    "components": {
        "securitySchemes": {
            "BearerAuth": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT"
            }
        }
    },
    "security": [{"BearerAuth": []}],
    "tags": [
        {"name": "Autenticação", "description": "Endpoints para login e registro"},
        {"name": "Postagens", "description": "Gerenciamento de postagens"},
        {"name": "Comentários", "description": "Gerenciamento de comentários"},
        {"name": "Curtidas", "description": "Gerenciamento de curtidas"},
        {"name": "Usuários", "description": "Gerenciamento de usuários"}
    ],
    "swagger_ui": True,
    "specs": [
        {
            "endpoint": "apispec",
            "route": "/apispec.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],    
    "static_url_path": "/flasgger_static",
    "specs_route": "/apidocs/"    
}