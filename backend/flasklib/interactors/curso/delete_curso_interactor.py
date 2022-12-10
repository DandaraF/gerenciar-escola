from dataclasses import dataclass
from typing import List

from flasklib.domain import Curso
from flasklib.interactors.exceptions import CursoNotFoundException


class DeleteCursoRequestModel:
    def __init__(self, curso_id: str):
        self.curso_id = curso_id


@dataclass
class DeleteCursoResponseModel:
    curso: Curso


class DeleteCursoInteractor:
    def __init__(self,
                 request: DeleteCursoRequestModel,
                 curso_adapter,
                 materia_adapter):
        self.request = request
        self.curso_adapter = curso_adapter
        self.materia_adapter = materia_adapter

    def run(self):
        curso = self._get_curso()

        return DeleteCursoResponseModel(curso)

    def _deletar_curso(self):
        curso = self._get_curso()
        curso.delete()

        return curso

    def _get_curso(self):
        curso = self.curso_adapter.get_by_id(self.request.curso_id)

        if not curso:
            raise CursoNotFoundException("Curso não encontrado!")

        return curso


