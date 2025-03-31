from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from

from services.curtida_service import curtir_postagem, descurtir_postagem, contabilizar_curtidas_por_postagem, listar_quem_curtiu_postagem

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
    id_usuario = get_jwt_identity()
    
    sucesso = curtir_postagem(id_postagem, id_usuario)

    if not sucesso:
        return jsonify({"error": "Você já curtiu essa postagem"}), 400

    return jsonify({"message": "Postagem curtida com sucesso!"}), 201

@curtida_bp.route("/postagem/<int:id_postagem>/descurtir", methods=["DELETE"])
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
    id_usuario = get_jwt_identity()

    sucesso = descurtir_postagem(id_postagem, id_usuario)

    if not sucesso:
        return jsonify({"error": "Você ainda não curtiu essa postagem"}), 400

    return jsonify({"message": "Curtida removida com sucesso!"}), 200

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
def quantos_curtiram_postagem(id_postagem):
    total = contabilizar_curtidas_por_postagem(id_postagem)

    return jsonify({"id_postagem": id_postagem, "curtidas": total}), 200

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
def quem_curtiu_postagem(id_postagem):
    result = listar_quem_curtiu_postagem(id_postagem)
    
    return jsonify(result), 200