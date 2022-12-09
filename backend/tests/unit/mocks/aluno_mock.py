from flasklib.domain import Aluno
from tests.unit.mocks import endereco_mock


def aluno_mock():
    return Aluno(nome="nome",
                 cpf="cpf",
                 endereco=endereco_mock(),
                 telefone="2312341234",
                 curso_id="12",
                 ativo=True)
