from . import db


class Produto(db.Model):

    __tablename__ = 'produtos'


    Produto_id = db.column(db.Interge, primary_key = True, autoincrement =True)
    produto_nome = db.column(db.String(100), nullable = False)
    produto_preco = db.column(db.Numeric(10,2), nullable = False)
    