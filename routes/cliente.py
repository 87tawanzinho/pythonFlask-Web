from flask import Blueprint, render_template 


cliente_route = Blueprint('cliente', __name__)



@cliente_route.route('/') # rota principal clientes
def lista_clientes():
    return {"pagina": "Lista_clientes"}



@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    pass

@cliente_route.route('/new')
def form_cliente():
    return {"pagina": "lista_new"}

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    pass


@cliente_route.route('/<int:cliente_id>/edit', methods=['PUT'])
def editar_cliente(cliente_id):
    pass

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    pass


@cliente_route.route('/<int:cliente_id>/delete', methods=['PUT'])
def deletar_cliente(cliente_id):
    pass
