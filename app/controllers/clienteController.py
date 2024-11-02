from flask import blueprint, request, jsonify
from models import db, Cliente


cliente_bp = blueprint('cliente' ,__name__)

@cliente_bp.route('/cliente', methods =['POST'])
def criar_cliente():
    data = request.json
    novo_cliente = Cliente(cliente_nome = data['cliente_nome'], cliente_email = data['cliente_email'])
    db.session.add(novo_cliente)
    db.session.commit()
    return jsonify({'id': novo_cliente.cliente_id, 'cliente_nome': novo_cliente.cliente_nome, 'cliente_email': novo_cliente.cliente_email}),201


@cliente_bp.route('/cliente', methods =['GET'])
def listar_cliente():
    cliente = Cliente.query.all()
    listar_cliente = ({'id': cliente.cliente_id, 'nome': cliente.clinte_nome, 'email': cliente.cliente_email} for cliente in clientes)
    return jsonify(listar_cliente)

@cliente_bp.route('/cliente/<int:id>', methods = ['PUT'])
def atualizar_clientes():
    data = request.json
    cliente = Cliente.query.get(id)
    if not cliente:
        return jsonify('erro: cliente não encontrado'), 404
    
    cliente.cliente_email = data = ['cliente_email']
    db.session.commit()
    return jsonify({'id': cliente.cliente_id, 'nome': cliente.cliente_nome, 'email': cliente.cliente_email}), 200
    

@cliente_bp.route('/cliente/<inte:id>', methods = ['DELETE'])
def deletar_cliente():
    cliente = Cliente.query.get(id)

    if not cliente:
        return jsonify({'erro': 'cliente não existe'}), 404
    

    db.session.delete(cliente)
    db.session.commit()
    return jsonify({'message': 'cliente deletado com sucesso '})
    


