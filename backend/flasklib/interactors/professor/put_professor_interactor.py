from dataclasses import dataclass

from flasklib.domain import Professor, Endereco
from flasklib.interactors.exceptions import ProfessorNotFoundException


class PutProfessorRequestModel:
    def __init__(self,
                 professor_id: str,
                 nome: str,
                 cpf: str,
                 endereco: dict,
                 telefone: str,
                 curso_id: str,
                 materia_id: str,
                 ativo: bool):
        self.professor_id = professor_id
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.curso_id = curso_id
        self.materia_id = materia_id
        self.ativo = ativo


@dataclass
class PutProfessorResponseModel:
    professor: Professor


class PutProfessorInteractor:
    def __init__(self,
                 request: PutProfessorRequestModel,
                 professor_adapter):
        self.request = request
        self.professor_adapter = professor_adapter

    def run(self):
        professor_id = self._get_professor_id()

        professor_atualizado = self._atualizar_professor(professor_id)

        return PutProfessorResponseModel(professor_atualizado)

    def _atualizar_professor(self, professor_id: str):
        endereco = self._instancia_endereco()

        professor = Professor(nome=self.request.nome,
                              cpf=self.request.cpf,
                              endereco=endereco,
                              telefone=self.request.telefone,
                              curso_id=self.request.curso_id,
                              materia_id=self.request.materia_id)

        professor.entity_id = professor_id

        professor.set_adapter(self.professor_adapter)
        professor.save()

        return professor

    def _instancia_endereco(self):
        return Endereco.from_json(self.request.endereco)

    def _get_professor_id(self):
        professor = self.professor_adapter.get_by_id(self.request.professor_id)

        if not professor:
            raise ProfessorNotFoundException("Professor não encontrado!")

        return professor.entity_id
