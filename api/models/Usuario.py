from db.database import db

class Usuario(db.Model):
    __tablename__ = "Usuarios"
    
    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Login = db.Column(db.String(80), unique=True, nullable=False)
    Senha = db.Column(db.String(255), nullable=False)