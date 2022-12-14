from dataclasses import dataclass

from flasklib.domain import Professor
from flasklib.interactors.exceptions import ProfessorNotFoundException


class DeleteProfessorRequestModel:
    def __init__(self, professor_id: str):
        self.professor_id = professor_id


@dataclass
class DeleteProfessorResponseModel:
    professor: Professor


class DeleteProfessorInteractor:
    def __init__(self,
                 request: DeleteProfessorRequestModel,
                 professor_adapter):
        self.request = request
        self.professor_adapter = professor_adapter

    def run(self):
        professor = self._get_professor()
        professor.soft_delete()

        return DeleteProfessorResponseModel(professor)

    def _get_professor(self):
        professor = self.professor_adapter.get_by_id(self.request.professor_id)

        if not professor:
            raise ProfessorNotFoundException("Professor não encontrado!")

        return professor
