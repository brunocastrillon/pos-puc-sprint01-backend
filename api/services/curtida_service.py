from db.database import db
from models.Curtida import Curtida

def curtir_postagem(id_postagem, id_usuario):
    curtida_existente = Curtida.query.filter_by(Id_Postagem=id_postagem, Id_Usuario=id_usuario).first()
    
    if curtida_existente:
        return None  # O usuário já curtiu essa postagem

    curtir = Curtida(Id_Postagem=id_postagem, Id_Usuario=id_usuario)
    
    db.session.add(curtir)
    db.session.commit()
    
    return True

def descurtir_postagem(id_postagem, id_usuario):
    curtida_existente = Curtida.query.filter_by(Id_Postagem=id_postagem, Id_Usuario=id_usuario).first()

    if not curtida_existente:
        return None  # O usuário não curtiu essa postagem

    db.session.delete(curtida_existente)
    db.session.commit()
    
    return True

def contabilizar_curtidas_por_postagem(id_postagem):
    count = Curtida.query.filter_by(Id_Postagem=id_postagem).count()
    
    return count

def listar_quem_curtiu_postagem(id_postagem):
    curtidas = Curtida.query.filter_by(Id_Postagem=id_postagem).all()

    usuarios = [
        {
            "id": curtida.Usuario.Id,
            "username": curtida.Usuario.Login
        }
        for curtida in curtidas if curtida.Usuario
    ]

    return {
        "id_postagem": id_postagem,
        "cutidas": len(usuarios),
        "usuarios": usuarios
    }