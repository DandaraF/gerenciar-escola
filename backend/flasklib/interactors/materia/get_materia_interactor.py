from dataclasses import dataclass
from typing import List

from flasklib.domain import Materia


@dataclass
class GetMateriasResponseModel:
    materias: List[Materia]


class GetMateriasInteractor:
    def __init__(self, materia_adapter):
        self.materia_adapter = materia_adapter

    def run(self):
        materias = self._get_materias()

        return GetMateriasResponseModel(materias)

    def _get_materias(self):
        return self.materia_adapter.list_all()
