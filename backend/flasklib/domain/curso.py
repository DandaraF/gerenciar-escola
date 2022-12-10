from enum import Enum
from typing import List

from marshmallow import fields, post_load
from marshmallow_enum import EnumField

from basic import BasicEntity


class Periodo(Enum):
    MATUTINO = "matutino"
    DIURNO = "diurno"
    NOTURNO = "noturno"


class Curso(BasicEntity):
    def __init__(self,
                 nome: str,
                 materias_ids: List[str],
                 carga_horaria: int,
                 ementa: str,
                 professores_ids,
                 periodo: Periodo,
                 entity_id=None):
        super().__init__(entity_id=entity_id)
        self.nome = nome
        self.materias_ids = materias_ids
        self.carga_horaria = carga_horaria
        self.ementa = ementa
        self.professores_ids = professores_ids
        self.periodo = periodo

    class Schema(BasicEntity.Schema):
        nome = fields.Str(required=True)
        materias_ids = fields.List(fields.Str,
                                   load_default=[],
                                   dump_default=[])
        carga_horaria = fields.Integer(required=True)
        ementa = fields.String(required=True)
        professores_ids = fields.List(fields.Str,
                                      load_default=[],
                                      dump_default=[])
        periodo = EnumField(Periodo,
                            required=True,
                            by_value=True)

        # noinspection PyUnusedLocal
        @post_load
        def post_load(self, data, **kwargs):
            return Curso(**data)
