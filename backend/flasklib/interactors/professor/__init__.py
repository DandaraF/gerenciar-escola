from .delete_professor_interactor import (DeleteProfessorResponseModel,
                                          DeleteProfessorInteractor,
                                          DeleteProfessorRequestModel)
from .get_professores_interactor import (GetProfessoresInteractor,
                                         GetProfessoresRequestModel,
                                         GetProfessoresResponseModel)
from .post_professor_interactor import (PostProfessorRequestModel,
                                        PostProfessorInteractor,
                                        PostProfessorResponseModel)
from .put_professor_interactor import (PutProfessorResponseModel,
                                       PutProfessorInteractor,
                                       PutProfessorRequestModel)

__all__ = [
    'DeleteProfessorResponseModel',
    'DeleteProfessorInteractor',
    'DeleteProfessorRequestModel',

    'GetProfessoresResponseModel',
    'GetProfessoresRequestModel',
    'GetProfessoresInteractor',

    'PostProfessorResponseModel',
    'PostProfessorInteractor',
    'PostProfessorRequestModel',

    'PutProfessorResponseModel',
    'PutProfessorRequestModel',
    'PutProfessorInteractor'
]
