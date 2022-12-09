from flasklib.domain import Professor
from tests.unit.mocks import endereco_mock


def professor_mock():
    return Professor(nome="nome",
                     cpf="cpf",
                     endereco=endereco_mock(),
                     telefone="2312341234",
                     curso_id="12",
                     materia_id="3234",
                     ativo=True)
