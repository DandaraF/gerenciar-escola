from unittest import TestCase

from tests.unit.domain.util import general_roundtrip
from tests.unit.mocks.aluno_mock import aluno_mock


class TestAluno(TestCase):
    def test_aluno_roundtrip(self):
        aluno = aluno_mock()

        self.assertEqual(aluno, general_roundtrip(aluno))
