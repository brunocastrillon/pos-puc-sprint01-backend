from flask import Blueprint, request, jsonify
from flasgger import swag_from

from services.autenticar_service import autenticar_usuario, registrar_usuario

autenticar_bp = Blueprint("autenticar", __name__)

@autenticar_bp.route("/autenticar/login", methods=["POST"])
@swag_from({
    "tags": ["Autenticação"],
    "summary": "alguma coisa",
    "description": "alguma coisa",
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "login": {"type": "string"},
                        "senha": {"type": "string"}
                    },
                    "example": {
                        "login": "usuario1",
                        "senha": "senha123"
                    }
                }
            }
        }
    },
    "responses": {
        200: {"description": "Token JWT retornado"},
        401: {"description": "Credenciais inválidas"},
        415: {"description": "Content-Type incorreto"}
    }
})
def autenticar():
    if not request.is_json:
        return jsonify({"error": "o corpo da requisição deve ser JSON"}), 415
    
    data = request.json
    autenticacao = autenticar_usuario(data["login"], data["senha"])

    if not autenticacao:
        return jsonify({"error": "credenciais inválidas"}), 401
    
    return jsonify(autenticacao), 200

@autenticar_bp.route("/autenticar/registrar", methods=["POST"])
@swag_from({
    "tags": ["Autenticação"],
    "summary": "alguma coisa",
    "description": "alguma coisa",
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "login": {"type": "string"},
                        "senha": {"type": "string"}
                    },
                    "example": {
                        "login": "usuario",
                        "senha": "123",
                    }
                }
            }
        }
    },
    "responses": {
        201: {"description": "login registrado com sucesso"},
        400: {"description": "Usuário já existe"}
    }
})
def registrar():
    data = request.json
    usuario = registrar_usuario(data["login"], data["senha"])
    return jsonify({"message": "usuário registrado com sucesso", "id": usuario.Id}), 201