from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from

from services.comentario_service import criar_comentario, deletar_comentario, editar_comentario, listar_comentarios_por_postagem

comentario_bp = Blueprint("comentario", __name__)

@comentario_bp.route("/comentario", methods=["POST"])
@jwt_required()
@swag_from({
    "tags": ["Comentário"],
    "summary": "Novo Comentário",
    "description": "Realiza a inserção de um novo registro na tabela Comentarios",
    "security": [{"BearerAuth": []}],
    "requestBody": {
        "required": True,
        "content": {
            "application/json": {
                "schema": {
                    "type": "object",
                    "properties": {
                        "id_postagem": {"type": "integer"},
                        "conteudo": {"type": "string"}
                    },
                    "example": {
                        "id_postagem": "0",
                        "conteudo": "conteudo exemlo",
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
    id_usuario = get_jwt_identity()
    data = request.json

    comentario = criar_comentario(data["conteudo"], data["id_postagem"], id_usuario)

    return jsonify({"message": "Comentário criado!", "id": comentario.Id}), 201

@comentario_bp.route("/comentario/<int:id_comentario>", methods=["DELETE"])
@jwt_required()
@swag_from({
    "tags": ["Comentário"],
    "summary": "Exclusão de um comentário",
    "description": "Realiza a remoção de um registro na tabela Comentarios",
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
def deletar(id_comentario):
    id_usuario = get_jwt_identity()
    removido = deletar_comentario(id_comentario)

    if not removido:
        return jsonify({"error": "Comentário não encontrado"}), 404

    return jsonify({"message": "Comentário excluído!"}), 200

@comentario_bp.route("/comentario/<int:id_comentario>", methods=["PUT"])
@jwt_required()
@swag_from({
    "tags": ["Comentário"],
    "summary": "Edição de um comentário",
    "description": "Realiza a edição de um registro na tabela Comentarios",
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
                        "conteudo": {"type": "string"}
                    },
                    "example": {
                        "conteudo": "conteudo exemlo",
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
def editar(id_comentario):
    id_usuario = get_jwt_identity()
    data = request.json
    
    comentario = editar_comentario(data["conteudo"], id_comentario)

    if not comentario:
        return jsonify({"error": "comentário não encontrado"}), 404

    return jsonify({"message": "Comentário atualizado!", "id": comentario.Id}), 200

@comentario_bp.route("/postagem/<int:id_postagem>/comentarios", methods=["GET"])
@jwt_required()
@swag_from({
    "tags": ["Comentário"],
    "summary": "Lista de comentários de uma postagem",
    "description": "Realiza uma consulta na tabela Comentarios retornando uma lista de comentários vinculado a uma determinada postagem",
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
def listar_por_postagem(id_postagem): 
    comments = listar_comentarios_por_postagem(id_postagem)
    return jsonify(comments), 200