from flasklib.domain import Endereco


def endereco_mock():
    return Endereco(cep="1231243",
                    logradouro="Rua chrome",
                    numero="12",
                    bairro="Lua",
                    cidade="Mundo",
                    estado="SP",
                    complemento="5")
