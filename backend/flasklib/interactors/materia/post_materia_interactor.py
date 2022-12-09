from dataclasses import dataclass

from flasklib.domain import Materia


class PostMateriaRequestModel:
    def __init__(self, nome: str):
        self.nome = nome


@dataclass
class PostMateriaResponseModel:
    materia: Materia


class PostMateriaInteractor:
    def __init__(self,
                 request: PostMateriaRequestModel,
                 materia_adapter):
        self.request = request
        self.materia_adapter = materia_adapter

    def run(self):
        materia = self._cadastrar_materia()

        return PostMateriaResponseModel(materia)

    def _cadastrar_materia(self):
        materia = Materia(nome=self.request.nome)

        materia.set_adapter(self.materia_adapter)
        materia.save()

        return materia
