from uuid import uuid4

from marshmallow import Schema, fields


class BasicValue:
    @classmethod
    def from_json(cls, dict_data):
        return cls.Schema().load(dict_data)

    def to_json(self):
        return self.Schema().dump(self)

    def __eq__(self, other):
        return all([getattr(self, attr) == getattr(other, attr)
                    for attr in self.Schema().fields.keys()])

    class Schema(Schema):
        ...


class BasicEntity(BasicValue):
    def __init__(self, entity_id=None):
        self.entity_id = entity_id or str(uuid4())
        self.adapter = None

    def set_adapter(self, adapter):
        self.adapter = adapter

    def save(self):
        my_entity_id = self.adapter.save(self.to_json())
        return my_entity_id

    def delete(self):
        self.adapter.delete(self.entity_id)

    def __eq__(self, other):
        return self.entity_id == other.entity_id

    def __hash__(self):
        return hash(self.entity_id)

    class Schema(Schema):
        entity_id = fields.String(required=True, allow_none=True)
