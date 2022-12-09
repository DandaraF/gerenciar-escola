from marshmallow import fields, post_load

from basic import BasicEntity


class Materia(BasicEntity):
    def __init__(self,
                 nome: str,
                 entity_id=None):
        super().__init__(entity_id=entity_id)
        self.nome = nome

    class Schema(BasicEntity.Schema):
        nome = fields.Str(required=True)

        # noinspection PyUnusedLocal
        @post_load
        def post_load(self, data, **kwargs):
            return Materia(**data)
