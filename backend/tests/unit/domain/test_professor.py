from unittest import TestCase

from tests.unit.domain.util import general_roundtrip
from tests.unit.mocks import professor_mock


class TestProfessor(TestCase):
    def test_professor_roundtrip(self):
        mock_professor = professor_mock()

        self.assertEqual(mock_professor, general_roundtrip(mock_professor))
