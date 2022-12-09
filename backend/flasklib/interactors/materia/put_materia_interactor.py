from dataclasses import dataclass

from flasklib.domain import Materia
from flasklib.interactors.exceptions import MateriaNotFoundException


class PutMateriaRequestModel:
    def __init__(self,
                 materia_id: str,
                 nome: str):
        self.materia_id = materia_id
        self.nome = nome


@dataclass
class PutMateriaResponseModel:
    materia: Materia


class PutMateriaInteractor:
    def __init__(self,
                 request: PutMateriaRequestModel,
                 materia_adapter):
        self.request = request
        self.materia_adapter = materia_adapter

    def run(self):
        materia_id = self._get_materia_id()

        materia_atualizado = self._atualizar_materia(materia_id)

        return PutMateriaResponseModel(materia_atualizado)

    def _atualizar_materia(self, materia_id: str):
        materia = Materia(nome=self.request.nome)

        materia.entity_id = materia_id

        materia.set_adapter(self.materia_adapter)
        materia.save()

        return materia

    def _get_materia_id(self):
        materia = self.materia_adapter.get_by_id(self.request.materia_id)

        if not materia:
            msg = "Matéria não encontrada ao tentar altera-lá"
            raise MateriaNotFoundException(msg)

        return materia.entity_id
