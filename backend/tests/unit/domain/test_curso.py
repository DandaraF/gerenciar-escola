from unittest import TestCase

from tests.unit.domain.util import general_roundtrip
from tests.unit.mocks import curso_mock


class TestCurso(TestCase):
    def test_curso_roundtrip(self):
        mock_curso = curso_mock()

        self.assertEqual(mock_curso, general_roundtrip(mock_curso))
