from dataclasses import dataclass

from flasklib.domain import Aluno
from flasklib.interactors.exceptions import AlunoNotFoundException


class DeleteAlunoRequestModel:
    def __init__(self,
                 aluno_id: str):
        self.aluno_id = aluno_id


@dataclass
class DeleteAlunoResponseModel:
    aluno: Aluno


class DeleteAlunoInteractor:
    def __init__(self,
                 request: DeleteAlunoRequestModel,
                 aluno_adapter):
        self.request = request
        self.aluno_adapter = aluno_adapter

    def run(self):
        aluno = self._get_aluno()
        aluno.soft_delete()

        return DeleteAlunoResponseModel(aluno)

    def _get_aluno(self):
        aluno = self.aluno_adapter.get_by_id(self.request.aluno_id)

        if not aluno:
            raise AlunoNotFoundException("Aluno não encontrado!")

        return aluno
