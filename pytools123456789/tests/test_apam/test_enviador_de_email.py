import pytest
from pytools123456789.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br', 'marcosas.soares2@gmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'marcosas37@hotmail.com',
        'Curso Python Pro.',
        'Pytools'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'destinatario',
    ['', 'marcosas.soares2']
)
def test_remetente_invalido(destinatario):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            destinatario,
            'marcosas37@hotmail.com',
            'Curso Python Pro.',
            'Pytools'
        )
