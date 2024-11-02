from . import db

class Usuario(db.model):

    __tablename__ = 'usuarios'


    usuarios_id = db.column(db.Integer, primary_key = True, autocrement = True)
    usuario_nome = db.column(db.String(100), nullable = False)
    senha = db.column(db.String(100), nullable = False)

    