from dataclasses import dataclass

from flasklib.domain import Professor, Endereco


class PostProfessorRequestModel:
    def __init__(self,
                 nome: str,
                 cpf: str,
                 endereco: dict,
                 telefone: str,
                 materia_id: str,
                 curso_id: str):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.materia_id = materia_id
        self.curso_id = curso_id


@dataclass
class PostProfessorResponseModel:
    professor: Professor


class PostProfessorInteractor:
    def __init__(self,
                 request: PostProfessorRequestModel,
                 professor_adapter):
        self.request = request
        self.professor_adapter = professor_adapter

    def run(self):
        professor = self._cadastrar_professor()

        return PostProfessorResponseModel(professor)

    def _cadastrar_professor(self):
        endereco = self._instancia_endereco()

        professor = Professor(nome=self.request.nome,
                              cpf=self.request.cpf,
                              endereco=endereco,
                              telefone=self.request.telefone,
                              curso_id=self.request.curso_id,
                              materia_id=self.request.materia_id)

        professor.set_adapter(self.professor_adapter)
        professor.save()

        return professor

    def _instancia_endereco(self):
        return Endereco.from_json(self.request.endereco)
