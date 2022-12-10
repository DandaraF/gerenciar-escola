from dataclasses import dataclass
from typing import List

from flasklib.domain import Professor, Materia, Curso, Endereco


class GetProfessoresRequestModel:
    def __init__(self, ativo: bool):
        self.ativo = ativo


@dataclass
class ResponseProfessor:
    entity_id: str
    nome: str
    cpf: str
    endereco: Endereco
    telefone: str
    curso: Curso
    materia: Materia
    ativo: bool


@dataclass
class GetProfessoresResponseModel:
    professores: List[ResponseProfessor]


class GetProfessoresInteractor:
    def __init__(self,
                 request: GetProfessoresRequestModel,
                 professor_adapter,
                 materia_adapter,
                 curso_adapter):
        self.request = request
        self.professor_adapter = professor_adapter
        self.materia_adapter = materia_adapter
        self.curso_adapter = curso_adapter

    def run(self):
        professores = self._get_professores_ativos()

        return GetProfessoresResponseModel(professores)

    def _get_professores(self):
        professores: List[Professor] = self.professor_adapter.list_all()

        return [ResponseProfessor(entity_id=p.entity_id,
                                  nome=p.nome,
                                  cpf=p.cpf,
                                  endereco=p.endereco,
                                  telefone=p.telefone,
                                  curso=self._get_curso_by_id(p.curso_id),
                                  materia=self._get_materia_by_id(
                                      p.materia_id),
                                  ativo=p.ativo)
                for p in professores]

    def _get_professores_ativos(self):
        professores = self._get_professores()

        if self.request.ativo is True:
            return [professor for professor in professores
                    if professor.ativo is True]

        if self.request.ativo is False:
            return [professor for professor in professores
                    if professor.ativo is False]

        return professores

    def _get_materia_by_id(self, materia_id: str):
        return self.materia_adapter.get_by_id(materia_id)

    def _get_curso_by_id(self, curso_id: str):
        return self.curso_adapter.get_by_id(curso_id)
