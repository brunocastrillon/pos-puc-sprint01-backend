from db.database import db
from models.Usuario import Usuario
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

def autenticar_usuario(login, senha):
    usuario = Usuario.query.filter_by(Login=login).first()

    if usuario and check_password_hash(usuario.Senha, senha):
        token = create_access_token(identity=str(usuario.Id))
        return {"token": token, "id_usuario": usuario.Id}
    
    return None

def registrar_usuario(login, senha):
    senha_cript = generate_password_hash(senha)

    usuario = Usuario(Login=login, Senha=senha_cript)
 
    db.session.add(usuario)
    db.session.commit()
    
    return usuario
