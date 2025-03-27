from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from flasgger import swag_from

from services.postagem_service import criar, deletar, editar, listar_por_usuario, listar_todos

postagem_bp = Blueprint("postagem", __name__)

@postagem_bp.route("/postagem", methods=["POST"])
@jwt_required()
@swag_from({
    "tags": ["Postagem"],
    "summary": "",
    "description": "",
    "security": [{"BearerAuth": []}],
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "content": {"type": "string"}
                    },
                    "example": {
                        "title": "titulo exemplo",
                        "content": "conteudo exemlo",
                    }
                }
            }
        }
    },
    "responses": {
        201: {"description": "Postagem criada com sucesso"},
        401: {"description": "Acesso negado"}
    }
})
def criar():
    pass

@postagem_bp.route("/postagem/<int:id_postagem>", methods=["DELETE"])
@jwt_required()
@swag_from({
    "tags": ["Postagem"],
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
        200: {"description": "Postagem excluída com sucesso"},
        401: {"description": "Acesso negado"},
        404: {"description": "Postagem não encontrada"}
    }
})
def deletar():
    pass

@postagem_bp.route("/postagem/<int:id_postagem>", methods=["PUT"])
@jwt_required()
@swag_from({
    "tags": ["Postagem"],
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
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "content": {"type": "string"}
                    },
                    "example": {
                        "title": "titulo exemplo",
                        "content": "conteudo exemlo",
                    }
                }
            }
        }
    },    
    "responses": {
        200: {"description": "Postagem atualizada com sucesso"},
        404: {"description": "Postagem não encontrada"},
        401: {"description": "Acesso negado"}
    }
})
def editar():
    pass

@postagem_bp.route("/usuario/postagem", methods=["GET"])
@jwt_required()
@swag_from({
    "tags": ["Postagem"],
    "summary": "",
    "description": "",
    "security": [{"BearerAuth": []}],
    "responses": {
        200: {"description": "Lista de postagem do usuário"},
        401: {"description": "Acesso negado"}
    }
})
def listar_por_usuario():
    pass

@postagem_bp.route("/postagem", methods=["GET"])
@jwt_required()
@swag_from({
    "tags": ["Postagem"],
    "summary": "",
    "description": "",
    "security": [{"BearerAuth": []}],
    "responses": {
        200: {"description": "Lista de postagem"},
        401: {"description": "Acesso negado"}
    }
})
def listar_todos():
    pass
