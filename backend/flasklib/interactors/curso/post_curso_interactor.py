from dataclasses import dataclass
from typing import List

from flasklib.domain import Curso
from flasklib.domain.curso import Periodo
from flasklib.interactors.exceptions import PeriodoInvalidException


class PostCursoRequestModel:
    def __init__(self,
                 nome: str,
                 materias_ids: List[str],
                 carga_horaria: int,
                 ementa: str,
                 professores_ids,
                 periodo: str):
        self.nome = nome
        self.materias_ids = materias_ids
        self.carga_horaria = carga_horaria
        self.ementa = ementa
        self.professores_ids = professores_ids
        self.periodo = periodo


@dataclass
class PostCursoResponseModel:
    curso: Curso


class PostCursoInteractor:
    def __init__(self,
                 request: PostCursoRequestModel,
                 curso_adapter):
        self.request = request
        self.curso_adapter = curso_adapter

    def run(self):
        curso = self._cadastrar_curso()

        return PostCursoResponseModel(curso)

    def _get_periodo(self):
        if self.request.periodo == Periodo.MATUTINO.value:
            return Periodo.MATUTINO

        if self.request.periodo == Periodo.DIURNO.value:
            return Periodo.DIURNO

        if self.request.periodo == Periodo.NOTURNO.value:
            return Periodo.NOTURNO

        raise PeriodoInvalidException("Periodo inválido")

    def _cadastrar_curso(self):
        curso = Curso(nome=self.request.nome,
                      materias_ids=self.request.materias_ids,
                      carga_horaria=self.request.carga_horaria,
                      ementa=self.request.ementa,
                      professores_ids=self.request.professores_ids,
                      periodo=self._get_periodo())

        curso.set_adapter(self.curso_adapter)
        curso.save()

        return curso
