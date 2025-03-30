from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from

from services.comentario_service import criar_comentario, deletar_comentario, editar_comentario, listar_comentarios_por_postagem

comentario_bp = Blueprint("comentario", __name__)

@comentario_bp.route("/comentario", methods=["POST"])
@jwt_required()
@swag_from({
    "tags": ["Comentário"],
    "summary": "alguma coisa",
    "description": "alguma coisa",
    "security": [{"BearerAuth": []}],
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "post_id": {"type": "integer"},
                        "content": {"type": "string"}
                    },
                    "example": {
                        "post_id": "0",
                        "content": "conteudo exemlo",
                    }
                }
            }
        }
    },
    "responses": {
        201: {"description": "Comentário criado"},
        401: {"description": "Acesso negado"}
    }
})
def criar():
    pass

@comentario_bp.route("/comentario/<int:id_comentario>", methods=["DELETE"])
@jwt_required()
@swag_from({
    "tags": ["Comentário"],
    "summary": "",
    "description": "",
    "security": [{"BearerAuth": []}],
    "parameters": [
        {
            "name": "id_comentario",
            "in": "path",
            "required": True,
            "type": "integer"
        }
    ],
    "responses": {
        200: {"description": "Comentário excluído"},
        401: {"description": "Acesso negado"}
    }
})
def deletar():
    pass

@comentario_bp.route("/comentario/<int:id_comentario>", methods=["PUT"])
@jwt_required()
@swag_from({
    "tags": ["Comentário"],
    "summary": "",
    "description": "",
    "security": [{"BearerAuth": []}],
    "parameters": [
        {
            "name": "id_comentario",
            "in": "path",
            "required": True,
            "type": "integer"
        },
    ],    
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "content": {"type": "string"}
                    },
                    "example": {
                        "content": "conteudo exemlo",
                    }
                }
            }
        }
    },
    "responses": {
        200: {"description": "Comentário atualizado"},
        401: {"description": "Acesso negado"}
    }
})
def editar():
    pass

@comentario_bp.route("/postagem/<int:id_postagem>/comentarios", methods=["GET"])
@jwt_required()
@swag_from({
    "tags": ["Comentário"],
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
        200: {"description": "Lista de comentários"},
        401: {"description": "Acesso negado"}
    }
})
def listar_por_postagem():
    pass