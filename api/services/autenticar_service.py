from db.database import db
from models.Usuario import Usuario
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

def autenticar(login, senha):
    pass

def registrar(login, senha):
    pass
