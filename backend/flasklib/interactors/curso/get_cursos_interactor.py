from dataclasses import dataclass
from typing import List

from flasklib.domain import Curso, Materia, Professor


@dataclass
class CursoModel:
    entity_id: str
    nome: str
    materias: List[Materia]
    carga_horaria: int
    ementa: str
    professores: List[Professor]
    periodo: str


@dataclass
class GetCursosResponseModel:
    cursos: List[CursoModel]


class GetCursosInteractor:
    def __init__(self,
                 curso_adapter,
                 materia_adapter,
                 professor_adapter):
        self.curso_adapter = curso_adapter
        self.materia_adapter = materia_adapter
        self.professor_adapter = professor_adapter

    def run(self):
        cursos = self._get_cursos()

        return GetCursosResponseModel(cursos)

    def _get_cursos(self):
        cursos: List[Curso] = self.curso_adapter.list_all()

        return [CursoModel(entity_id=c.entity_id,
                           nome=c.nome,
                           materias=self._get_materias_by_ids(c.materias_ids),
                           carga_horaria=c.carga_horaria,
                           ementa=c.ementa,
                           professores=self._get_professores(
                               c.professores_ids),
                           periodo=c.periodo.value)
                for c in cursos]

    def _get_materias_by_ids(self, materias_ids: List[str]):
        return [self.materia_adapter.get_by_id(x) for x in materias_ids]

    def _get_professores(self, professores_ids: List[str]):
        return [self.professor_adapter.get_by_id(x)
                for x in professores_ids]
