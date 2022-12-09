from dataclasses import dataclass

from flasklib.domain import Materia
from flasklib.interactors.exceptions import MateriaNotFoundException


class DeleteMateriaRequestModel:
    def __init__(self,
                 materia_id: str):
        self.materia_id = materia_id


@dataclass
class DeleteMateriaResponseModel:
    materia: Materia


class DeleteMateriaInteractor:
    def __init__(self,
                 request: DeleteMateriaRequestModel,
                 materia_adapter):
        self.request = request
        self.materia_adapter = materia_adapter

    def run(self):
        materia = self._get_materia()
        materia.soft_delete()

        return DeleteMateriaResponseModel(materia)

    def _get_materia(self):
        materia = self.materia_adapter.get_by_id(self.request.materia_id)

        if not materia:
            msg = "Matéria não encontrada ao deleta-lá"
            raise MateriaNotFoundException(msg)

        return materia
