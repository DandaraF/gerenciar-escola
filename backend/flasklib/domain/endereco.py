from typing import Optional

from marshmallow import post_load, fields

from basic import BasicValue


class Endereco(BasicValue):
    def __init__(self,
                 cep: str,
                 logradouro: str,
                 numero: str,
                 bairro: str,
                 cidade: str,
                 estado: str,
                 complemento: Optional[str] = None):
        self.cep = cep
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado

    class Schema(BasicValue.Schema):
        cep = fields.Str(required=True)
        logradouro = fields.Str(required=True)
        numero = fields.Str(required=True)
        complemento = fields.Str(required=False,
                                 allow_none=True)
        bairro = fields.Str(required=True)
        cidade = fields.Str(required=True)
        estado = fields.Str(required=True)

        # noinspection PyUnusedLocal
        @post_load
        def on_load(self, data, **kwargs):
            return Endereco(**data)
