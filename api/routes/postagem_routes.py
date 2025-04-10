from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from flasgger import swag_from

from services.postagem_service import criar_postagem, deletar_postagem, editar_postagem, listar_postagens_por_usuario, listar_todas_postagens, obter_postagem

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
                        "titulo": {"type": "string"},
                        "conteudo": {"type": "string"}
                    },
                    "example": {
                        "titulo": "titulo exemplo",
                        "conteudo": "conteudo exemlo",
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
    id_usuario = get_jwt_identity()

    data = request.json
    postagem = criar_postagem(data["titulo"], data["conteudo"], id_usuario)

    return jsonify({"message": "postagem criada com sucesso", "id": postagem.Id}), 201

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
        403: {"description": "Você não é o autor desta postagem"},
        404: {"description": "Postagem não encontrada"},
        500: {"description": "erro de processamento"}
    }
})
def deletar(id_postagem):
    id_usuario = get_jwt_identity()
    postagem = obter_postagem(id_postagem)

    if not postagem:
        return jsonify({"error": "Postagem não encontrada"}), 404    

    if postagem["id_usuario"] != int(id_usuario):
        return jsonify({"error": "Você não é o autor desta postagem. Portanto, não tem permissão para edita-la"}), 403
    
    removido = deletar_postagem(id_postagem)

    if not removido:
        return jsonify({"error": "Erro ao tentar remover esta postagem"}), 500
    
    return jsonify({"message": "Postagem excluída com sucesso!"}), 200

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
                        "titulo": {"type": "string"},
                        "conteudo": {"type": "string"}
                    },
                    "example": {
                        "titulo": "titulo exemplo",
                        "conteudo": "conteudo exemlo",
                    }
                }
            }
        }
    },    
    "responses": {
        200: {"description": "Postagem atualizada com sucesso"},
        403: {"description": "Você não é o autor desta postagem"},
        404: {"description": "Postagem não encontrada"}
    }
})
def editar(id_postagem):
    id_usuario = get_jwt_identity()
    postagem = obter_postagem(id_postagem)

    if not postagem:
        return jsonify({"error": "Postagem não encontrada"}), 404
    
    if postagem["id_usuario"] != int(id_usuario):
        return jsonify({"error": "Você não é o autor desta postagem. Portanto, não tem permissão para edita-la"}), 403
    
    data = request.json
    postagem_editada = editar_postagem(data["titulo"], data["conteudo"], id_postagem)

    if not postagem_editada:
        return jsonify({"error": "Erro ao atualizar postagem"}), 500
    
    return jsonify({"message": "Postagem atualizada com sucesso!", "id": postagem_editada.Id}), 200

@postagem_bp.route("/postagem/usuario", methods=["GET"])
@jwt_required()
@swag_from({
    "tags": ["Postagem"],
    "summary": "",
    "description": "",
    "security": [{"BearerAuth": []}],
    "responses": {
        200: {"description": "Lista de postagem do usuário"},
        401: {"description": "Acesso negado"},
        404: {"description": "Postagens não encontradas"}
    }
})
def listar_por_usuario():
    id_usuario = get_jwt_identity()
    postagens = listar_postagens_por_usuario(id_usuario)
    
    if postagens is None:
        return jsonify({"error": "Postagens não encontradas"}), 404
    
    return jsonify(postagens), 200

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
    postagens = listar_todas_postagens()
    return jsonify(postagens), 200
