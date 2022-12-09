from dataclasses import dataclass

from flasklib.domain import Aluno, Endereco


class PostAlunoRequestModel:
    def __init__(self,
                 nome: str,
                 cpf: str,
                 endereco: dict,
                 telefone: str,
                 curso_id: str):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.curso_id = curso_id


@dataclass
class PostAlunoResponseModel:
    aluno: Aluno


class PostAlunoInteractor:
    def __init__(self,
                 request: PostAlunoRequestModel,
                 aluno_adapter):
        self.request = request
        self.aluno_adapter = aluno_adapter

    def run(self):
        aluno = self._cadastrar_aluno()

        return PostAlunoResponseModel(aluno)

    def _cadastrar_aluno(self):
        endereco = self._instancia_endereco()

        aluno = Aluno(nome=self.request.nome,
                      cpf=self.request.cpf,
                      endereco=endereco,
                      telefone=self.request.telefone,
                      curso_id=self.request.curso_id)

        aluno.set_adapter(self.aluno_adapter)
        aluno.save()

        return aluno

    def _instancia_endereco(self):
        return Endereco.from_json(self.request.endereco)
