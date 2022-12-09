from dataclasses import dataclass
from typing import List

from flasklib.domain import Aluno


class GetAlunosRequestModel:
    def __init__(self, ativo: bool):
        self.ativo = ativo


@dataclass
class GetAlunosResponseModel:
    alunos: List[Aluno]


class GetAlunosInteractor:
    def __init__(self,
                 request: GetAlunosRequestModel,
                 aluno_adapter):
        self.request = request
        self.aluno_adapter = aluno_adapter

    def run(self):
        alunos = self._get_alunos_filtrados()

        return GetAlunosResponseModel(alunos)

    def _get_alunos(self):
        return self.aluno_adapter.list_all()

    def _get_alunos_filtrados(self):
        alunos = self._get_alunos()

        if self.request.ativo is True:
            return [aluno for aluno in alunos
                    if aluno.ativo is True]

        if self.request.ativo is False:
            return [aluno for aluno in alunos
                    if aluno.ativo is False]

        return alunos

