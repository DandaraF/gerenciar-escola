from dataclasses import dataclass
from typing import List

from flasklib.domain import Professor


class GetProfessoresRequestModel:
    def __init__(self, ativo: bool):
        self.ativo = ativo


@dataclass
class GetProfessoresResponseModel:
    professores: List[Professor]


class GetProfessoresInteractor:
    def __init__(self,
                 request: GetProfessoresRequestModel,
                 professor_adapter):
        self.request = request
        self.professor_adapter = professor_adapter

    def run(self):
        professores = self._get_professores_filtrados()

        return GetProfessoresResponseModel(professores)

    def _get_professores(self):
        return self.professor_adapter.list_all()

    def _get_professores_filtrados(self):
        professores = self._get_professores()

        if self.request.ativo is True:
            return [professor for professor in professores
                    if professor.ativo is True]

        if self.request.ativo is False:
            return [professor for professor in professores
                    if professor.ativo is False]

        return professores

