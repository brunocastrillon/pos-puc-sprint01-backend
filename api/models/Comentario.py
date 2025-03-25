from db.database import db

class Comentario(db.Model):
    __tablename__ = "Comentarios"

    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    Id_Postagem = db.Column(db.Integer, db.ForeignKey("Postagens.Id"), nullable=False)
    Id_Usuario = db.Column(db.Integer, db.ForeignKey("Usuarios.Id"), nullable=False)

    Conteudo = db.Column(db.Text, nullable=False)
    Data_Criacao = db.Column(db.DateTime, default=db.func.current_timestamp())
    Data_Edicao = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
    Postagem = db.relationship("Postagem", backref="Comentarios")
    Autor = db.relationship("Usuario", backref="Comentarios")