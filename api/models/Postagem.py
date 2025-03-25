from db.database import db

class Postagem(db.Model):
    __tablename__ = "Postagens"
    
    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    Id_Usuario = db.Column(db.Integer, db.ForeignKey("Usuarios.Id"), nullable=False)

    Titulo = db.Column(db.String(255), nullable=False)
    Conteudo = db.Column(db.Text, nullable=False)
    Data_Criacao = db.Column(db.DateTime, default=db.func.current_timestamp())

    Autor = db.relationship("Usuario", backref="Postagens")