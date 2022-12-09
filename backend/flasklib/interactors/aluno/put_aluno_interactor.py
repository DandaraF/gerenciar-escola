from dataclasses import dataclass

from flasklib.domain import Aluno, Endereco
from flasklib.interactors.exceptions import AlunoNotFoundException


class PutAlunoRequestModel:
    def __init__(self,
                 aluno_id: str,
                 nome: str,
                 cpf: str,
                 endereco: dict,
                 telefone: str,
                 curso_id: str,
                 ativo: bool):
        self.aluno_id = aluno_id
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.curso_id = curso_id
        self.ativo = ativo


@dataclass
class PutAlunoResponseModel:
    aluno: Aluno


class PutAlunoInteractor:
    def __init__(self,
                 request: PutAlunoRequestModel,
                 aluno_adapter):
        self.request = request
        self.aluno_adapter = aluno_adapter

    def run(self):
        aluno_id = self._get_aluno_id()

        aluno_atualizado = self._atualizar_aluno(aluno_id)

        return PutAlunoResponseModel(aluno_atualizado)

    def _atualizar_aluno(self, aluno_id: str):
        endereco = self._instancia_endereco()

        aluno = Aluno(nome=self.request.nome,
                      cpf=self.request.cpf,
                      endereco=endereco,
                      telefone=self.request.telefone,
                      curso_id=self.request.curso_id)

        aluno.entity_id = aluno_id

        aluno.set_adapter(self.aluno_adapter)
        aluno.save()

        return aluno

    def _instancia_endereco(self):
        return Endereco.from_json(self.request.endereco)

    def _get_aluno_id(self):
        aluno = self.aluno_adapter.get_by_id(self.request.aluno_id)

        if not aluno:
            raise AlunoNotFoundException("Aluno não encontrado!")

        return aluno.entity_id
