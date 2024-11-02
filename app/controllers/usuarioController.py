from flask import Blueprint, request, jsonify
from models  import usuario
from models import db

usuario_bp = Blueprint('usuarios', __name__)

@usuario_bp.route('/usuario', methods = ['POST'])
def criar_usuraio():
    data = request.json
    novo_usuario = Usuario(usuario_nome = data['usuario_nome'], senha = data = ['senha'])
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({'id': novo_usuario.usuario_id, 'nome': novo_usuario.usario_nome }), 201


@usuario_bp.route('/usuario', methods = ['GET'])
def listar_usuarios():
    data = request.json
    usuario = Usuario.query.all()
    lista_usuario = ({'usuario_id': u.usuario_id, 'usuario_nome': u.usuario.nome} for u in usuarios)


@usuario_bp.route('/usuario/<int:id>', methods = ['PUT'])
def atualizar_usuario():
    data = request.json
    usuario = Usuario.query.get(id)
    
    if not usuario:
        return jsonify ({'erro': 'usuario não encontrado'}), 404

    usuario.usuario_nome = data['usuario']
    db.session.commit()
    return jsonify({'id': usuario.usuario_id, 'nome': usuario.usuario_nome}), 200

@usuario_bp.route('/usuario/<int:id>', methods = ['DELETE'])
def deletar_usuario():
    usuario = Usuario.query.get(id)

    if not usuario:
        return jsonify({'ERRO': 'usuario não encontrado '}), 404
    
    db.session.delete(usuario)
    db.session.commit
    return jsonify({'message' 'USUARIO DELETADO COM SUCESSO'}), 204



