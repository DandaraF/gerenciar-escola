from dataclasses import dataclass
from typing import List

from flasklib.domain import Aluno, Endereco, Curso


class GetAlunosRequestModel:
    def __init__(self, ativo: bool):
        self.ativo = ativo


@dataclass
class ResponseAluno:
    entity_id: str
    nome: str
    cpf: str
    endereco: Endereco
    telefone: str
    curso: Curso
    ativo: bool


@dataclass
class GetAlunosResponseModel:
    alunos: List[ResponseAluno]


class GetAlunosInteractor:
    def __init__(self,
                 request: GetAlunosRequestModel,
                 aluno_adapter,
                 curso_adapter):
        self.request = request
        self.aluno_adapter = aluno_adapter
        self.curso_adapter = curso_adapter

    def run(self):
        alunos = self._get_alunos_filtrados()

        return GetAlunosResponseModel(alunos)

    def _get_alunos(self):
        alunos: List[Aluno] = self.aluno_adapter.list_all()

        return [ResponseAluno(entity_id=a.entity_id,
                              nome=a.nome,
                              cpf=a.cpf,
                              endereco=a.endereco,
                              telefone=a.telefone,
                              curso=self._get_curso_by_id(a.curso_id),
                              ativo=a.ativo)
                for a in alunos]

    def _get_alunos_filtrados(self):
        alunos = self._get_alunos()

        if self.request.ativo is True:
            return [aluno for aluno in alunos
                    if aluno.ativo is True]

        if self.request.ativo is False:
            return [aluno for aluno in alunos
                    if aluno.ativo is False]

        return alunos

    def _get_curso_by_id(self, curso_id: str):
        return self.curso_adapter.get_by_id(curso_id)
