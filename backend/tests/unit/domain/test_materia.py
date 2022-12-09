from unittest import TestCase

from tests.unit.domain.util import general_roundtrip
from tests.unit.mocks.materia_mock import materia_mock


class TestMateria(TestCase):
    def test_materia_roundtrip(self):
        mock_materia = materia_mock()

        self.assertEqual(mock_materia, general_roundtrip(mock_materia))
