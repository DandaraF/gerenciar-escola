from flasklib.domain import Curso
from flasklib.domain.curso import Periodo


def curso_mock():
    return Curso(nome="nome",
                 materias_id=["2", "3"],
                 carga_horaria=300,
                 ementa="2",
                 professores_ids="2",
                 periodo=Periodo.DIURNO)
