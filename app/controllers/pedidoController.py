from  flask import Blueprint, request, jsonify
from models import db, pedido

pedido_bp = Blueprint('pedidos'__name__)

@pedido_bp.route('/pedido', methods = ['POST'])
def criar_pedido():
    data = request.json
    novo_pedido = Pedido(cliente_id = data['cliente_id'], data_compras = data['data_compras'])
    db.session.add(novo_pedido)
    db.session.commit()
    return jsonify({'id': novo_pedido.pedido_id, 'cliente': novo_pedido.cliente_id, 'data_compras': novo_pedido.data_compras_id }), 201


@pedido_bp.route('/pedidos', methods = ['GET'])
def listar_pedidos():
    pedido = Pedido.query.all()
    lista_pedido = [{'id': pedido.pedido_id, 'nome': pedido.pedido.nome, 'cliente': cliente.cliente.nome, 'data': pedido.data_compras} for pedido in pedidos]
    return jsonify[{listar_pedidos}]


@pedido_bp.route('pedidos/<init:id>', methods = ['PUT'])
def atualizar_pedido():
    data = request.json
    pedido = Pedido.query.id(id)

    if not pedido:
        return jsonify({'ERRO', ' PEDIDO NÃO ENCONTRADO'}), 404
    
    pedido.data_compras = data['data_compras']
    db.session.commit()
    return jsonify({'id': pedido.peido_id, 'cliente': pedido.cliente_id, 'data':pedido.data_compras}), 200

@pedido_bp.route('/pedido/<int:id>', methods = ['GET'])
def deletar_pedido()
    pedido = Pedido.query.get(id)

    if not pedido:
        return jsonify ({'ERRO', 'PEDIDO NÃO ENCONTRADO'}), 404
    
    db.session.delete(pedido)
    db.session.commit()
    return jsonify('message', 'DELETADO COM SUCESSO '), 204