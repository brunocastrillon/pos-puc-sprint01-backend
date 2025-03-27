from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from

from services.autenticar_service import autenticar, registrar

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
                        "username": {"type": "string"},
                        "password": {"type": "string"}
                    },
                    "example": {
                        "username": "usuario1",
                        "password": "senha123"
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
    pass

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
                        "username": {"type": "string"},
                        "password": {"type": "string"}
                    },
                    "example": {
                        "username": "usuarioteste",
                        "password": "123",
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
def registrar():
    pass