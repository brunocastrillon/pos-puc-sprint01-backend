from db.database import db

class Curtida(db.Model):
    __tablename__ = "Curtidas"

    Id = db.Column(db.Integer, primary_key=True)

    Id_Postagem = db.Column(db.Integer, db.ForeignKey("Postagens.Id"), nullable=False)
    Id_Usuario = db.Column(db.Integer, db.ForeignKey("Usuarios.Id"), nullable=False)

    Usuario = db.relationship("Usuario", backref="Curtidas")
    Postagem = db.relationship("Postagem", backref="Curtidas")

    __table_args__ = (db.UniqueConstraint("Id_Usuario", "Id_Postagem", name="Curtida_Unica"),)  # Garante que um usuário só possa curtir uma vez
