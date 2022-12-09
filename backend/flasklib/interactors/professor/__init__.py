from .delete_professor_interactor import (DeleteProfessorResponseModel,
                                          DeleteProfessorInteractor,
                                          DeleteProfessorRequestModel)
from .get_professors_interactor import (GetProfessorsInteractor,
                                        GetProfessorsRequestModel,
                                        GetProfessorsResponseModel)
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

    'GetProfessorsResponseModel',
    'GetProfessorsRequestModel',
    'GetProfessorsInteractor',

    'PostProfessorResponseModel',
    'PostProfessorInteractor',
    'PostProfessorRequestModel',

    'PutProfessorResponseModel',
    'PutProfessorRequestModel',
    'PutProfessorInteractor'
]
