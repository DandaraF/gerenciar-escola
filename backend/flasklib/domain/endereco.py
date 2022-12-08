from typing import Optional

from marshmallow import post_load, Schema


class Endereco:
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

    class Schema(Schema):
        ...

        # noinspection PyUnusedLocal
        @post_load
        def on_load(self, data, **kwargs):
            return Endereco(**data)
