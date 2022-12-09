from marshmallow import fields, post_load
from todaobra_domain import Endereco

from basic import BasicEntity


class Professor(BasicEntity):
    def __init__(self,
                 nome: str,
                 cpf: str,
                 endereco: Endereco,
                 telefone: str,
                 curso_id: str,
                 materia_id: str,
                 ativo: bool = True,
                 entity_id=None):
        super().__init__(entity_id=entity_id)
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.curso_id = curso_id
        self.materia_id = materia_id
        self.ativo = ativo

    class Schema(BasicEntity.Schema):
        nome = fields.Str(required=True)
        cpf = fields.Str(required=True)
        endereco = fields.Nested(Endereco.Schema,
                                 allow_none=False,
                                 required=True)
        telefone = fields.Str(required=True)
        curso_id = fields.Str(required=True)
        materia_id = fields.Str(required=True)
        ativo = fields.Bool(allow_none=False,
                            load_default=True)

        # noinspection PyUnusedLocal
        @post_load
        def post_load(self, data, **kwargs):
            return Professor(**data)
