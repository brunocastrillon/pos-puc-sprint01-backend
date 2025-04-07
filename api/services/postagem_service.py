from db.database import db
from models.Postagem import Postagem
from models.Usuario import Usuario
from models.Curtida import Curtida

def criar_postagem(titulo, conteudo, id_usuario):
    postagem = Postagem(Id_Usuario=id_usuario, Titulo=titulo, Conteudo=conteudo)

    db.session.add(postagem)
    db.session.commit()
    
    return postagem

def deletar_postagem(id_postagem):
    postagem = Postagem.query.get(id_postagem)

    if not postagem:
        return False

    db.session.delete(postagem)
    db.session.commit()

    return True

def editar_postagem(titulo, conteudo, id_postagem):
    postagem = Postagem.query.get(id_postagem)

    if not postagem:
        return None
    
    postagem.Titulo = titulo
    postagem.Conteudo = conteudo

    db.session.commit()
    return postagem

def listar_todas_postagens():
    postagens = (
        db.session.query(
            Postagem.Id,
            Postagem.Titulo,
            Postagem.Conteudo,
            Postagem.Data_Criacao,
            Usuario.Login.label("Autor"),
            db.func.count(Curtida.Id).label("Curtidas")
        )
        .join(Usuario, Postagem.Id_Usuario == Usuario.Id)
        .outerjoin(Curtida, Postagem.Id == Curtida.Id_Postagem)
        .group_by(Postagem.Id, Usuario.Login)
        .order_by(Postagem.Data_Criacao.desc())
        .all()
    )

    return [
        {
            "id": postagem.Id,
            "titulo": postagem.Titulo,
            "conteudo": postagem.Conteudo,
            "autor": postagem.Autor,
            "criado_em": postagem.Data_Criacao,
            "curtidas": postagem.Curtidas
        }
        for postagem in postagens
    ]

def listar_postagens_por_usuario(id_usuario):
    usuario = Usuario.query.get(id_usuario)
    
    if not usuario:
        return None

    postagens = Postagem.query.filter_by(Id_Usuario=id_usuario).all()
    
    return [
        {
            "id": postagem.Id,
            "titulo": postagem.Titulo,
            "conteudo": postagem.Conteudo,
            "criado_em": postagem.Data_Criacao
        }
        for postagem in postagens
    ]

def obter_postagem(id_postagem):
    postagem = Postagem.query.join(Usuario).filter(Postagem.Id == id_postagem).first()

    if not postagem:
        return None
    
    return {
        "id": postagem.Id,
        "titulo": postagem.Titulo,
        "conteudo": postagem.Conteudo,
        "id_usuario": postagem.Id_Usuario,
        "autor": postagem.Autor.Login,
        "criado_em": postagem.Data_Criacao
    }