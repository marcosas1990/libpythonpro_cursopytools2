from unittest.mock import Mock

import pytest
from pytools123456789.spam.enviador_de_email import Enviador
from pytools123456789.spam.main import EnviadorDeSpam
from pytools123456789.spam.modelos import Usuario


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Marcos', email='marcosas.soares2@gmail.com'),
            Usuario(nome='Luciano', email='marcosas.soares2@gmail.com')
        ],
        [
            Usuario(nome='Marcos', email='marcosas.soares2@gmail.com'),
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'marcosas.soares2@gmail.com',
        'Curso Python Pro',
        'Python Pro'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Marcos', email='marcosas.soares2@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luciano@email.com',
        'Curso Python Pro',
        'Python Pro'
    )
    enviador.enviar.assert_called_once_with(
        'luciano@email.com',
        'marcosas.soares2@gmail.com',
        'Curso Python Pro',
        'Python Pro'
    )
