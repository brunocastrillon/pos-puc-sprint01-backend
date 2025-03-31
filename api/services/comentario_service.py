from db.database import db
from models.Comentario import Comentario

def criar_comentario(conteudo, id_postagem, id_usuario):
    comentario = Comentario(Id_Usuario=id_usuario, Id_Postagem=id_postagem, Conteudo=conteudo)
   
    db.session.add(comentario)
    db.session.commit()

    return comentario

def deletar_comentario(id_comentario):
    comentario = Comentario.query.get(id_comentario)
    
    if not comentario:
        return False

    db.session.delete(comentario)
    db.session.commit()

    return True

def editar_comentario(conteudo, id_comentario):
    comentario = Comentario.query.get(id_comentario)

    if not comentario:
        return None

    comentario.Conteudo = conteudo
    db.session.commit()

    return comentario

def listar_comentarios_por_postagem(id_postagem):
    comentarios = db.session.query(Comentario).filter(Comentario.Id_Postagem == id_postagem).all()
    
    return [
        {
            "id": comentario.Id,
            "autor": comentario.Autor.Login if comentario.Autor else "Desconhecido",
            "id_postagem": comentario.Id_Postagem,
            "conteudo": comentario.Conteudo,
            "criado_em": comentario.Data_Criacao
        }
        for comentario in comentarios
    ]