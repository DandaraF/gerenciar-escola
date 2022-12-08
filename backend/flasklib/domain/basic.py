from uuid import uuid4

from marshmallow import Schema, fields


class BasicEntity:
    def __init__(self, entity_id=None):
        self.entity_id = entity_id or str(uuid4())

    class Schema(Schema):
        entity_id = fields.String(required=False,
                                  allow_none=True,
                                  missing=str(uuid4()))
