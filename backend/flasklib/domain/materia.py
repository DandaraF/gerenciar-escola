from marshmallow import fields, Schema, post_load

from flasklib.domain import BasicEntity


class Materia(BasicEntity):
    def __init__(self,
                 nome: str,
                 entity_id=None):
        super().__init__(entity_id=entity_id)
        self.nome = nome

    class Schema(Schema):
        nome = fields.Str(required=True)

        @post_load
        def post_load(self, data, **kwargs):
            return Materia(**data)

