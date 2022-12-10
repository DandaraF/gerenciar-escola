from dataclasses import dataclass
from typing import List

from flasklib.domain import Curso
from flasklib.domain.curso import Periodo
from flasklib.interactors.exceptions import CursoNotFoundException, \
    PeriodoInvalidException


class PutCursoRequestModel:
    def __init__(self,
                 curso_id: str,
                 nome: str,
                 materias_ids: List[str],
                 carga_horaria: int,
                 ementa: str,
                 professores_ids,
                 periodo: str):
        self.curso_id = curso_id
        self.nome = nome
        self.materias_ids = materias_ids
        self.carga_horaria = carga_horaria
        self.ementa = ementa
        self.professores_ids = professores_ids
        self.periodo = periodo


@dataclass
class PutCursoResponseModel:
    curso: Curso


class PutCursoInteractor:
    def __init__(self,
                 request: PutCursoRequestModel,
                 curso_adapter):
        self.request = request
        self.curso_adapter = curso_adapter

    def run(self):
        curso_id = self._get_curso_id()

        curso_atualizado = self._atualizar_curso(curso_id)

        return PutCursoResponseModel(curso_atualizado)

    def _get_periodo(self):
        if self.request.periodo == Periodo.MATUTINO.value:
            return Periodo.MATUTINO

        if self.request.periodo == Periodo.DIURNO.value:
            return Periodo.DIURNO

        if self.request.periodo == Periodo.NOTURNO.value:
            return Periodo.NOTURNO

        raise PeriodoInvalidException("Periodo inválido")

    def _atualizar_curso(self, curso_id: str):
        curso = Curso(nome=self.request.nome,
                      materias_ids=self.request.materias_ids,
                      carga_horaria=self.request.carga_horaria,
                      ementa=self.request.ementa,
                      professores_ids=self.request.professores_ids,
                      periodo=self._get_periodo())

        curso.entity_id = curso_id

        curso.set_adapter(self.curso_adapter)
        curso.save()

        return curso

    def _get_curso_id(self):
        curso = self.curso_adapter.get_by_id(self.request.curso_id)

        if not curso:
            raise CursoNotFoundException("Curso não encontrado!")

        return curso.entity_id
