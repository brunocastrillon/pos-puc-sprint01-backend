from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from

from services.curtida_service import curtir_postagem, descurtir_postagem, listar_curtidas_por_postagem, listar_quem_curtiu_postagem

curtida_bp = Blueprint("curtida", __name__)

@curtida_bp.route("/postagem/<int:id_postagem>/curtir", methods=["POST"])
@jwt_required()
@swag_from({
    "tags": ["Curtida"],
    "summary": "",
    "description": "",
    "security": [{"BearerAuth": []}],
    "parameters": [
        {
            "name": "id_postagem",
            "in": "path",
            "required": True,
            "type": "integer"
        }
    ],
    "responses": {
        201: {"description": "Curtida adicionada"},
        400: {"description": "Usuário já curtiu essa postagem"},
        401: {"description": "Acesso negado"},
        404: {"description": "Postagem não encontrada"}
    }
})
def curtir(id_postagem):
    pass

@curtida_bp.route("/postagem/<int:id_postagem>/descurtit", methods=["DELETE"])
@jwt_required()
@swag_from({
    "tags": ["Curtida"],
    "summary": "",
    "description": "",
    "security": [{"BearerAuth": []}],
    "parameters": [
        {
            "name": "id_postagem",
            "in": "path",
            "required": True,
            "type": "integer"
        }
    ],
    "responses": {
        200: {"description": "Curtida removida"},
        400: {"description": "Usuário ainda não curtiu essa postagem"},
        401: {"description": "Acesso negado"},
        404: {"description": "Postagem não encontrada"}
    }
})
def descurtir(id_postagem):
    pass

@curtida_bp.route("/postagem/<int:id_postagem>/curtidas", methods=["GET"])
@jwt_required()
@swag_from({
    "tags": ["Curtida"],
    "summary": "",
    "description": "",
    "security": [{"BearerAuth": []}],    
    "parameters": [
        {
            "name": "id_postagem",
            "in": "path",
            "required": True,
            "type": "integer"
        }
    ],
    "responses": {
        200: {"description": "Número total de curtidas"},
        401: {"description": "Acesso negado"},
        404: {"description": "Postagem não encontrada"}
    }
})
def listar_por_postagem(id_postagem):
    pass

@curtida_bp.route("/postagem/<int:id_postagem>/quemcurtiu", methods=["GET"])
@jwt_required()
@swag_from({
    "tags": ["Curtida"],
    "summary": "",
    "description": "",
    "security": [{"BearerAuth": []}],
    "parameters": [
        {
            "name": "id_postagem",
            "in": "path",
            "required": True,
            "type": "integer"
        }
    ],
    "responses": {
        200: {"description": "Lista de usuários que curtiram"},
        401: {"description": "Acesso negado"},
        404: {"description": "Postagem não encontrada"}
    }
})
def listar_quem_curtiu_postagem(id_postagem):
    pass