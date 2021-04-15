from pytools123456789.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Marcos', email='marcosas.soares2@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Marcos', email='marcosas.soares2@gmail.com'),
        Usuario(nome='Luciano', email='marcosas.soares2@gmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
